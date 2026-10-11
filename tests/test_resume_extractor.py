from pathlib import Path

from parsers.resume_extractor import (
    extract_resume,
    clean_text
)


def test_clean_text():
    text = "Hello   World\n\n\nPython   SQL"

    result = clean_text(text)

    assert result == "Hello World\nPython SQL"


def test_extracted_resume_files_exist():
    extracted_folder = Path("data/extracted")

    files = list(extracted_folder.glob("*.txt"))

    assert len(files) == 10


def test_resume_text_is_not_empty():
    extracted_folder = Path("data/extracted")

    files = list(extracted_folder.glob("*.txt"))

    for file in files:
        text = file.read_text(encoding="utf-8")

        assert len(text.strip()) > 0


def test_resume_extraction_function():
    resume_files = list(Path("data/resumes").glob("*.pdf"))

    assert len(resume_files) == 10

    for resume_file in resume_files:
        text = extract_resume(resume_file)

        assert isinstance(text, str)
        assert len(text.strip()) > 0