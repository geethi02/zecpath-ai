import json

from section_classifier.resume_section_classifier import (
    detect_section_heading,
    segment_resume,
)


def test_section_heading_detection():
    assert detect_section_heading("SKILLS") == "skills"
    assert detect_section_heading("WORK EXPERIENCE") == "work_experience"
    assert detect_section_heading("EDUCATION") == "education"
    assert detect_section_heading("CERTIFICATIONS") == "certifications"
    assert detect_section_heading("PROJECTS") == "projects"
    assert detect_section_heading("PROFESSIONAL SUMMARY") == "professional_summary"


def test_unknown_heading():
    assert detect_section_heading("Random Heading") is None


def test_resume_segmentation():
    sample_resume = """
    PROFESSIONAL SUMMARY
    Data analyst with Python and SQL experience.

    EDUCATION
    MSc Data Science and Analytics
    Sample University

    WORK EXPERIENCE
    Data Analyst
    ABC Company

    SKILLS
    Python, SQL, Power BI

    PROJECTS
    Sales Dashboard

    CERTIFICATIONS
    Google Data Analytics
    """

    sections = segment_resume(sample_resume)

    section_names = [
        section["section"]
        for section in sections
    ]

    assert section_names == [
        "professional_summary",
        "education",
        "work_experience",
        "skills",
        "projects",
        "certifications",
    ]


def test_labeled_sample_file():
    """
    Verify that the labeled resume samples contain
    the expected section labels.
    """

    file_path = "data/section_labeled/resume_section_labels.json"

    with open(file_path, "r", encoding="utf-8") as file:
        labels = json.load(file)

    expected_sections = {
        "skills",
        "work_experience",
        "education",
        "certifications",
        "projects",
    }

    detected_sections = {
        item["section"]
        for item in labels
    }

    assert expected_sections.issubset(detected_sections)