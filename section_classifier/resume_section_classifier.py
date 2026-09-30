"""
Zecpath AI - Resume Section Classifier

Detects and classifies common resume section headings and
segments resume text into meaningful sections.
"""

import re


SECTION_PATTERNS = {
    "professional_summary": [
        "professional summary",
        "summary",
        "profile",
        "professional profile",
        "career summary",
    ],

    "skills": [
        "skills",
        "technical skills",
        "skills and technologies",
        "skills & technologies",
        "technical expertise",
        "core skills",
        "key skills",
        "technologies",
    ],

    "work_experience": [
        "work experience",
        "experience",
        "professional experience",
        "employment history",
        "career history",
        "work history",
    ],

    "education": [
        "education",
        "educational qualifications",
        "academic background",
        "academic qualifications",
        "education background",
    ],

    "certifications": [
        "certifications",
        "certificates",
        "professional certifications",
        "courses and certifications",
        "courses & certifications",
        "certifications & training",
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "key projects",
        "project experience",
        "projects & research",
    ],
}


def normalize_heading(text: str) -> str:
    """
    Normalize a possible resume section heading.

    Removes extra spaces, punctuation, and converts text to lowercase.
    """

    text = text.strip().lower()

    # Replace & with "and"
    text = text.replace("&", "and")

    # Remove punctuation
    text = re.sub(r"[^a-z0-9\s]", "", text)

    # Normalize multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def detect_section_heading(text: str):
    """
    Detect the resume section represented by a heading.

    Returns:
        Section label if detected, otherwise None.
    """

    normalized_text = normalize_heading(text)

    for section, headings in SECTION_PATTERNS.items():

        normalized_headings = [
            normalize_heading(heading)
            for heading in headings
        ]

        if normalized_text in normalized_headings:
            return section

    return None


def infer_section_from_content(text: str):
    """
    Infer a likely resume section from content when
    an explicit section heading is missing.

    This is a lightweight keyword-based NLP fallback.
    """

    if not text or not text.strip():
        return None

    normalized_text = text.lower()

    section_keywords = {
        "skills": [
            "python",
            "sql",
            "power bi",
            "excel",
            "pandas",
            "numpy",
            "machine learning",
            "programming",
            "database",
        ],

        "work_experience": [
            "intern",
            "employee",
            "worked at",
            "company",
            "responsible for",
            "developed",
            "analyzed",
            "experience",
        ],

        "education": [
            "bachelor",
            "master",
            "m.sc",
            "b.sc",
            "university",
            "college",
            "degree",
            "graduated",
        ],

        "certifications": [
            "certification",
            "certified",
            "certificate",
            "course completion",
        ],

        "projects": [
            "project",
            "developed a",
            "built a",
            "dashboard",
            "system",
            "application",
        ],

        "professional_summary": [
            "professional summary",
            "career objective",
            "career summary",
            "data analyst with",
            "software developer with",
            "experienced in",
        ],
    }

    scores = {}

    for section, keywords in section_keywords.items():

        score = 0

        for keyword in keywords:
            if keyword in normalized_text:
                score += 1

        scores[section] = score

    if not scores:
        return None

    best_section = max(scores, key=scores.get)

    if scores[best_section] == 0:
        return None

    return best_section


def classify_text_block(text: str):
    """
    Classify a text block based on its heading.

    The first non-empty line is treated as a possible section heading.
    """

    if not text or not text.strip():
        return None

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        return None

    detected_section = detect_section_heading(lines[0])

    if detected_section:
        return detected_section

    # Use content-based inference if no heading is detected
    return infer_section_from_content(text)


def segment_resume(text: str):
    """
    Split resume text into sections based on detected headings.

    Uses heading-based detection first and content-based
    inference as a fallback when a heading is missing.

    Also handles inline labels such as:
        AI/ML: Python, LangChain
        Databases: MySQL, PostgreSQL
    """

    lines = text.splitlines()

    sections = []
    current_section = None
    current_text = []

    # Common inline labels that may appear inside a section
    inline_labels = [
        "programming:",
        "bi:",
        "analytics:",
        "ai/ml:",
        "databases:",
    ]

    for line in lines:

        stripped_line = line.strip()

        if not stripped_line:
            continue

        # Check for a normal section heading
        detected_section = detect_section_heading(stripped_line)

        if detected_section:

            # Save previous section
            if current_section:
                sections.append(
                    {
                        "section": current_section,
                        "text": "\n".join(current_text).strip(),
                    }
                )

            # Start new section
            current_section = detected_section
            current_text = []

        elif current_section:

            # Handle inline labels inside the current section
            lower_line = stripped_line.lower()

            found_inline_label = False

            for label in inline_labels:

                if label in lower_line:

                    current_text.append(stripped_line)

                    found_inline_label = True
                    break

            if not found_inline_label:
                current_text.append(stripped_line)

        else:

            # No section has been detected yet.
            # Try content-based inference for resumes
            # where the heading may be missing.
            inferred_section = infer_section_from_content(
                stripped_line
            )

            if inferred_section:

                current_section = inferred_section
                current_text = [stripped_line]

    # Save final section
    if current_section:
        sections.append(
            {
                "section": current_section,
                "text": "\n".join(current_text).strip(),
            }
        )

    return sections


if __name__ == "__main__":

    # Path to the extracted resume
    resume_path = "data/extracted/RESUME 1.txt"

    # Read resume text
    with open(resume_path, "r", encoding="utf-8") as file:
        resume_text = file.read()

    # Segment the resume
    sections = segment_resume(resume_text)

    # Display detected sections
    print("Detected Resume Sections:")
    print("-" * 50)

    for section in sections:
        print(f"\n[{section['section']}]")
        print(section["text"])