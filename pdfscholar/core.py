from pydantic import BaseModel
from enum import Enum
from pypdf import PdfReader, PdfWriter
from typing import Optional, List
import os
import re
import json

class Status(str, Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    FINISHED = 'finished'

class Chapter(BaseModel):
    title: str
    first_page: int
    last_page: int
    status: Status

class Pdf(BaseModel):
    title: str
    length: int
    chapters: List[Chapter]

CHAPTERS_BASE_PATH = './chapters'

def make_safe_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "", name).strip(" .").replace(" ", "_")

def get_filename(chapter: Chapter) -> str:
    return f"{CHAPTERS_BASE_PATH}/{make_safe_filename(chapter.title)}.pdf"

def save_chapters(reader: PdfReader, chapters: List[Chapter]):
    os.makedirs(CHAPTERS_BASE_PATH, exist_ok=True)
    writer = PdfWriter()
    current_chapter = None

    for page_number, page in enumerate(reader.pages, start=1):
        if page_number < chapters[0].first_page:
            continue

        new_chapter = next((c for c in chapters if c.first_page == page_number), None)
        if new_chapter and new_chapter != current_chapter:
            if current_chapter:
                _write_chapter_to_file(writer, current_chapter)
                writer = PdfWriter()
            current_chapter = new_chapter

        writer.add_page(page)

    if current_chapter and writer.pages:
        _write_chapter_to_file(writer, current_chapter)

def _write_chapter_to_file(writer: PdfWriter, chapter: Chapter):
    with open(get_filename(chapter), "wb") as file:
        writer.write(file)

def initialize_pdf(file: str) -> Pdf:
    reader = PdfReader(file)

    # Function to get the page number from an outline item
    def get_page_number(page_ref):
        for page_number, page in enumerate(reader.pages, start=1):
            if page.indirect_reference == page_ref:
                return page_number
        return -1

    # Parse the outline
    try:
        raw_outlines = reader.outline
    except Exception:
        raise ValueError("Failed to read the PDF outline. Ensure the file has a valid outline.")

    chapters = []
    for item in raw_outlines:
        # Skip nested outlines (if item is a list, it's nested)
        if isinstance(item, list):
            continue

        # Extract chapter title and page number
        title = str(item.title).strip('"').strip("'")
        first_page = get_page_number(item.page)

        if first_page > 0:
            chapters.append(Chapter(title=title, first_page=first_page, last_page=-1, status=Status.PENDING))

    if not chapters:
        raise ValueError("No chapters found in the PDF.")

    # Assign last_page for each chapter
    for i in range(len(chapters) - 1):
        chapters[i].last_page = chapters[i + 1].first_page - 1

    chapters[-1].last_page = len(reader.pages)

    # Save the chapters as individual files
    save_chapters(reader, chapters)

    return Pdf(title=reader.metadata.title or "Untitled PDF", length=len(reader.pages), chapters=chapters)

def read_pdf_json(file: str) -> Pdf:
    with open(file, "r") as json_file:
        return Pdf.model_validate_json(json_file.read())

def save_pdf_json(pdf: Pdf):
    with open("pdf.json", "w") as pdfjson:
        pdfjson.write(pdf.model_dump_json(indent=4))

def change_chapter_status(pdf: Pdf, chapter_number: int, new_status: Status) -> Pdf:
    if 0 <= chapter_number < len(pdf.chapters):
        pdf.chapters[chapter_number].status = new_status
    return pdf
