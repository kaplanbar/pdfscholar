import click
from pdfscholar import core

@click.group()
def pdfscholar():
    """
    pdfscholar: A command-line tool for studying PDFs efficiently.
    """
    pass

@click.command()
@click.argument('pdf_file', type=click.Path(exists=True, resolve_path=True))
def init(pdf_file):
    """
    Initialize a PDF for studying and split it into chapters.
    """
    click.secho(f"Initializing PDF: {pdf_file}", fg="cyan", bold=True)
    pdf = core.initialize_pdf(pdf_file)
    core.save_pdf_json(pdf)
    click.secho("Successfully initialized the PDF", fg="green", bold=True)

@click.command()
@click.argument('chapter_number', type=int)
def open_chapter(chapter_number):
    """
    Open a chapter by its number.
    """
    pdf = core.read_pdf_json("pdf.json")
    click.secho("Run command below to open the chapter:", fg="yellow", bold=True)
    chapter = pdf.chapters[chapter_number]
    if chapter.status == core.Status.PENDING:
        chapter.status = core.Status.IN_PROGRESS
    core.save_pdf_json(pdf)
    click.secho(f"open {core.get_filename(chapter)}", fg="magenta")

@click.command()
def progress():
    """
    View the progress of all chapters.
    """
    pdf = core.read_pdf_json("pdf.json")
    display_progress(pdf)

@click.command()
@click.argument('chapter_number', type=int)
def mark_finished(chapter_number):
    """
    Mark a chapter as finished.
    """
    pdf = core.read_pdf_json("pdf.json")
    pdf = core.change_chapter_status(pdf, chapter_number, core.Status.FINISHED)
    core.save_pdf_json(pdf)
    click.secho(f"Marked Chapter {chapter_number} as finished.", fg="green", bold=True)
    display_progress(pdf)

@click.command()
@click.argument('chapter_number', type=int)
def unmark_finished(chapter_number):
    """
    Reset a finished chapter to pending.
    """
    click.secho(f"Resetting Chapter {chapter_number} to pending.", fg="yellow")
    pdf = core.read_pdf_json("pdf.json")
    pdf = core.change_chapter_status(pdf, chapter_number, core.Status.PENDING)
    core.save_pdf_json(pdf)
    display_progress(pdf)

def display_progress(pdf: core.Pdf):
    click.secho("Progress Overview:", fg="blue", bold=True)
    for i, chapter in enumerate(pdf.chapters):
        status_color = {
            core.Status.PENDING: "red",
            core.Status.IN_PROGRESS: "yellow",
            core.Status.FINISHED: "green"
        }[chapter.status]
        click.secho(f"{i}. {chapter.title} ({chapter.status.value})", fg=status_color)

pdfscholar.add_command(init)
pdfscholar.add_command(open_chapter)
pdfscholar.add_command(progress)
pdfscholar.add_command(mark_finished)
pdfscholar.add_command(unmark_finished)

if __name__ == "__main__":
    pdfscholar()
