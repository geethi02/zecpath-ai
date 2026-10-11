import re
from pathlib import Path

from pypdf import PdfReader
from docx import Document


INPUT_FOLDER = Path("data/resumes")
OUTPUT_FOLDER = Path("data/extracted")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)



def extract_from_pdf(file_path):
    """Extract text from a PDF resume."""

    reader = PdfReader(file_path)
    pages_text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            pages_text.append(page_text)

    return "\n".join(pages_text)




def extract_from_docx(file_path):
    """Extract text from a DOCX resume."""

    document = Document(file_path)
    paragraphs_text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            paragraphs_text.append(paragraph.text)

    return "\n".join(paragraphs_text)



def clean_text(text):
    """Clean and normalize extracted resume text."""

    # Normalize bullet points
    text = text.replace("•", "-")
    text = text.replace("▪", "-")
    text = text.replace("●", "-")

    # Remove extra spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove unnecessary spaces from lines
    lines = []

    for line in text.splitlines():
        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines).strip()


def extract_resume(file_path):
    """Extract and clean a PDF or DOCX resume."""

    file_type = file_path.suffix.lower()

    if file_type == ".pdf":
        raw_text = extract_from_pdf(file_path)

    elif file_type == ".docx":
        raw_text = extract_from_docx(file_path)

    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    return clean_text(raw_text)


def process_resumes():
    """Process all resumes in the input folder."""

    resume_files = list(INPUT_FOLDER.glob("*.pdf"))
    resume_files += list(INPUT_FOLDER.glob("*.docx"))

    print(f"Found {len(resume_files)} resume(s).")

    for resume_file in resume_files:

        try:
            cleaned_text = extract_resume(resume_file)

            output_file = OUTPUT_FOLDER / f"{resume_file.stem}.txt"

            output_file.write_text(
                cleaned_text,
                encoding="utf-8"
            )

            print(f"Extracted: {resume_file.name}")
            print(f"Saved: {output_file}")

        except Exception as error:
            print(f"Error processing {resume_file.name}: {error}")


if __name__ == "__main__":
    process_resumes()