import json
import re
from pathlib import Path

input_folder = Path("data/extracted")
output_folder = Path("data/structured")

output_folder.mkdir(parents=True, exist_ok=True)


def clean_text(text):
    """Clean extra spaces and line breaks."""
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()


def get_section(text, section_name, all_sections):
    """
    Extract content between one section heading and the next section heading.
    """

    section_pattern = "|".join(
        re.escape(section) for section in all_sections
    )

    pattern = rf"""
        (?im)
        ^\s*{re.escape(section_name)}\s*$
        (.*?)
        (?=^\s*(?:{section_pattern})\s*$|\Z)
    """

    match = re.search(pattern, text, re.DOTALL | re.VERBOSE)

    if match:
        return match.group(1).strip()

    return ""


def extract_name(text):
    """Get the first non-empty line."""
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    return lines[0] if lines else ""


def extract_location(text):
    """Try to find a location from the contact section."""
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    for line in lines[:5]:
        if "@" in line:
            continue

        if re.search(
            r"\b(Bengaluru|Bangalore|Kochi|Kannur|Chennai|Mumbai|"
            r"Hyderabad|Pune|Delhi|Kerala|Karnataka|Maharashtra|"
            r"Tamil Nadu|Telangana)\b",
            line,
            re.IGNORECASE
        ):
            return line

    return ""


def extract_email(text):
    match = re.search(
        r"[\w\.-]+@[\w\.-]+\.\w+",
        text
    )

    return match.group(0) if match else ""


def extract_phone(text):
    match = re.search(
        r"(?:Phone\s*:\s*)?(\+?\d[\d\s\-]{8,}\d)",
        text,
        re.IGNORECASE
    )

    return match.group(1).strip() if match else ""


def clean_list(text):
    """Convert section text into a clean list."""
    items = []

    for line in text.splitlines():

        line = line.strip()

        if not line:
            continue

        line = re.sub(r"^[•\-\*]\s*", "", line)

        if line:
            items.append(line)

    return items


def structure_resume(text):

    text = clean_text(text)

    sections = [
        "PROFESSIONAL SUMMARY",
        "SUMMARY",
        "EDUCATION",
        "EXPERIENCE",
        "WORK EXPERIENCE",
        "SKILLS",
        "TECHNICAL SKILLS",
        "PROJECTS",
        "PROJECT",
        "CERTIFICATIONS",
        "CERTIFICATION",
        "ACHIEVEMENTS",
        "ACHIEVEMENT"
    ]

    summary = ""

    for section in ["PROFESSIONAL SUMMARY", "SUMMARY"]:
        summary = get_section(text, section, sections)

        if summary:
            break

    education = get_section(
        text,
        "EDUCATION",
        sections
    )

    experience = ""

    for section in ["EXPERIENCE", "WORK EXPERIENCE"]:
        experience = get_section(text, section, sections)

        if experience:
            break

    skills = ""

    for section in ["SKILLS", "TECHNICAL SKILLS"]:
        skills = get_section(text, section, sections)

        if skills:
            break

    projects = ""

    for section in ["PROJECTS", "PROJECT"]:
        projects = get_section(text, section, sections)

        if projects:
            break

    certifications = ""

    for section in ["CERTIFICATIONS", "CERTIFICATION"]:
        certifications = get_section(text, section, sections)

        if certifications:
            break

    return {
        "name": extract_name(text),
        "location": extract_location(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "summary": summary,
        "education": clean_list(education),
        "experience": clean_list(experience),
        "skills": clean_list(skills),
        "projects": clean_list(projects),
        "certifications": clean_list(certifications)
    }


resume_files = list(input_folder.glob("*.txt"))

print(f"Found {len(resume_files)} resumes.\n")


for resume_file in resume_files:

    text = resume_file.read_text(
        encoding="utf-8"
    )

    structured_data = structure_resume(text)

    output_file = output_folder / f"{resume_file.stem}.json"

    output_file.write_text(
        json.dumps(
            structured_data,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    print(f"Structured: {resume_file.name}")
    print(f"Saved: {output_file}\n")


print("Done! All resumes have been structured.")