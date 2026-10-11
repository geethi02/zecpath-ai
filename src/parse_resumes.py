from pathlib import Path
from pypdf import PdfReader

resume_folder = Path("data/resumes")
output_folder = Path("data/extracted")

# Create extracted folder if it doesn't exist
output_folder.mkdir(parents=True, exist_ok=True)

resume_files = list(resume_folder.glob("*.pdf"))

print(f"Found {len(resume_files)} resumes.\n")

for resume_file in resume_files:

    reader = PdfReader(resume_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    # Create output filename
    output_file = output_folder / f"{resume_file.stem}.txt"

    # Save extracted text
    output_file.write_text(text, encoding="utf-8")

    print(f"Saved: {output_file}")