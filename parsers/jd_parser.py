import json
import re
from pathlib import Path


INPUT_FOLDER = Path("data/job_descriptions")
OUTPUT_FOLDER = Path("data/structured")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


# Common skill names that the parser can identify
SKILL_SYNONYMS = {
    "python": ["python"],
    "sql": ["sql", "mysql", "postgresql"],
    "power bi": ["power bi", "powerbi"],
    "excel": ["excel", "microsoft excel"],
    "tableau": ["tableau"],
    "machine learning": ["machine learning", "ml"],
    "data analysis": ["data analysis", "data analytics"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "java": ["java"],
    "javascript": ["javascript", "js"],
    "react": ["react", "react.js"],
    "aws": ["aws", "amazon web services"],
    "git": ["git", "github"]
}


def read_jd(file_path):
    """Read job description text."""

    return file_path.read_text(
        encoding="utf-8"
    )


def normalize_text(text):
    """Clean and normalize job description text."""

    text = text.replace("•", "-")
    text = text.replace("▪", "-")
    text = text.replace("●", "-")

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)

    return text.strip()


def extract_role(text):
    """Extract the job role from the job description."""

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    # Usually the first line contains the job title
    if lines:
        first_line = lines[0]

        if len(first_line.split()) <= 6:
            return first_line

    patterns = [
        r"(?:job title|role|position)\s*[:\-]\s*([^\n]+)",
        r"(?:looking for|hiring for|seeking)\s+(?:a|an)?\s*([A-Za-z][A-Za-z &/-]+?)(?:\s+to\s+|\s+who\s+|\s+with\s+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(1).strip()

    return ""


def extract_experience(text):
    """Extract minimum and maximum years of experience."""

    pattern = r"(\d+)\s*(?:-|to)\s*(\d+)\s*(?:years?|yrs?)"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return {
            "minimum_years": int(match.group(1)),
            "maximum_years": int(match.group(2))
        }

    pattern = r"(\d+)\+?\s*(?:years?|yrs?)\s*(?:of)?\s*experience"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return {
            "minimum_years": int(match.group(1)),
            "maximum_years": None
        }

    return {
        "minimum_years": None,
        "maximum_years": None
    }


def extract_education(text):
    """Extract common education requirements."""

    education = []

    patterns = {
        "Bachelor's degree": [
            r"bachelor'?s degree",
            r"bachelor'?s",
            r"\bb\.?s\.?\b",
            r"\bb\.?tech\b",
            r"\bb\.?e\.?\b"
        ],

        "Master's degree": [
            r"master'?s degree",
            r"master'?s",
            r"\bm\.?s\.?\b",
            r"\bm\.?tech\b",
            r"\bm\.?e\.?\b"
        ],

        "MBA": [
            r"\bmba\b"
        ],

        "PhD": [
            r"\bph\.?d\b"
        ]
    }

    for education_name, patterns_list in patterns.items():

        for pattern in patterns_list:

            if re.search(pattern, text, re.IGNORECASE):
                education.append(education_name)
                break

    return education


def extract_skills(text):
    """Identify required skills and normalize skill synonyms."""

    found_skills = []

    for standard_skill, synonyms in SKILL_SYNONYMS.items():

        for synonym in synonyms:

            pattern = r"\b" + re.escape(synonym) + r"\b"

            if re.search(pattern, text, re.IGNORECASE):
                found_skills.append(standard_skill)
                break

    return found_skills


def extract_keywords(text):
    """Extract important words from the JD."""

    keywords = []

    important_words = [
        "data",
        "analytics",
        "software",
        "developer",
        "engineer",
        "analyst",
        "machine learning",
        "artificial intelligence",
        "business",
        "marketing",
        "finance",
        "cloud"
    ]

    for word in important_words:

        if re.search(
            r"\b" + re.escape(word) + r"\b",
            text,
            re.IGNORECASE
        ):
            keywords.append(word)

    return keywords


def parse_job_description(text):
    """Convert raw JD text into a structured job requirement object."""

    text = normalize_text(text)

    structured_jd = {
        "job_title": extract_role(text),
        "experience": extract_experience(text),
        "education_required": extract_education(text),
        "required_skills": extract_skills(text),
        "keywords": extract_keywords(text),
        "normalized_text": text
    }

    return structured_jd


def process_job_descriptions():
    """Process all text job descriptions."""

    jd_files = list(INPUT_FOLDER.glob("*.txt"))

    print(f"Found {len(jd_files)} job description(s).")

    for jd_file in jd_files:

        try:
            raw_text = read_jd(jd_file)

            structured_data = parse_job_description(raw_text)

            output_file = (
                OUTPUT_FOLDER /
                f"{jd_file.stem}_structured.json"
            )

            output_file.write_text(
                json.dumps(
                    structured_data,
                    indent=4,
                    ensure_ascii=False
                ),
                encoding="utf-8"
            )

            print(f"Parsed: {jd_file.name}")
            print(f"Saved: {output_file}")

        except Exception as error:

            print(
                f"Error processing {jd_file.name}: {error}"
            )


if __name__ == "__main__":
    process_job_descriptions()