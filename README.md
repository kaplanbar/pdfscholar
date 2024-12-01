# pdfscholar

**pdfscholar** is a powerful command-line tool for studying PDF documents efficiently. It allows users to split PDFs into chapters, track progress through each chapter, and organize their study workflow. Designed with learners in mind, `pdfscholar` ensures a seamless and intuitive experience for managing educational or reference materials.

---

## Features

- **Automatic Chapter Splitting**: Automatically splits a PDF into individual chapter files during initialization.
- **Progress Tracking**: Tracks chapter statuses:
  - **Pending**: Chapters not started yet.
  - **In Progress**: Chapters currently being studied.
  - **Finished**: Chapters marked as completed.
- **Open Chapters Directly**: Open any chapter directly from the command line.
- **Automatic Progress Saving**: Progress is automatically saved after every action.

---

## Installation

Install `pdfscholar` using your favorite package manager:

### Using `pip`:
```bash
pip install pdfscholar
```

---

## Usage

### 1. Initialize and Split a PDF
Start by initializing `pdfscholar` with a PDF file. This automatically splits the document into chapters and sets up progress tracking:
```bash
pdfscholar init my_study_material.pdf
```

**Output:**
```
PDF initialized and split into chapters:
1. Introduction (Pending)
2. Basics (Pending)
...
```

The split chapter files are stored in the `./chapters/` directory.

---

### 2. Open a Chapter
To start studying a chapter, open it directly from the terminal. The chapter's status will be updated to **"In Progress"**:
```bash
pdfscholar open-chapter 1
```

**Output:**
```
Opening Chapter 1: "Introduction" (Pages 1-5)
Status updated to "In Progress."
```

---

### 3. Track Your Progress

#### View Progress:
Check the status of all chapters:
```bash
pdfscholar progress
```

**Output:**
```
Study Progress:
[*] 1. Introduction (In Progress)
[ ] 2. Basics (Pending)
[ ] 3. Advanced Topics (Pending)
```

#### Mark a Chapter as Finished:
Once you complete a chapter, mark it as finished:
```bash
pdfscholar mark-finished 1
```

**Output:**
```
Chapter "Introduction" marked as finished. Progress saved automatically.
```

#### Unmark a Finished Chapter:
If you want to revisit a chapter:
```bash
pdfscholar unmark-finished 1
```

**Output:**
```
Chapter "Introduction" reset to "Pending."
```

---

## Help and Documentation

To view all available commands and options:
```bash
pdfscholar --help
```

To get help for a specific command:
```bash
pdfscholar <command> --help
```

Example:
```bash
pdfscholar open --help
```

**Output:**
```
Usage: pdfscholar open <chapter_number>
Description: Opens the specified chapter in the default PDF viewer.
```

---

## Example Workflow

1. **Initialize and Split a PDF**:
   ```bash
   pdfscholar init textbook.pdf
   ```
   Output:
   ```
   PDF initialized and split into chapters:
   1. Introduction (Pending)
   2. Basics (Pending)
   ```

2. **Open and Study a Chapter**:
   ```bash
   pdfscholar open 1
   ```
   Output:
   ```
   Opening Chapter 1: "Introduction" (Pages 1-5)
   Status updated to "In Progress."
   ```

3. **Mark Chapter as Finished**:
   ```bash
   pdfscholar mark-finished 1
   ```
   Output:
   ```
   Chapter "Introduction" marked as finished.
   ```

4. **Check Progress**:
   ```bash
   pdfscholar progress
   ```
   Output:
   ```
   Study Progress:
   [ ] 1. Introduction (Finished)
   [*] 2. Basics (In Progress)
   [ ] 3. Advanced Topics (Pending)
   ```

---

## Future Features

- **Chapter Summarization**: Automatically generate summaries for each chapter.
- **Automatic Quizzes**: Create interactive exams based on the content of each chapter.
- **Multi-PDF Management**: Track progress across multiple PDFs.

---

Start studying smarter today with `pdfscholar`! 🎓