class ResumeNormalizer:
    """Normalize resume content into a standard format."""

    STANDARD_SECTIONS = [
        "summary",
        "skills",
        "experience",
        "education",
        "projects",
        "certifications",
    ]

    def normalize_text(self, text):
        """Clean and standardize resume text."""

        if not text:
            return ""

        lines = []

        for line in text.splitlines():
            clean_line = " ".join(line.strip().split())

            if clean_line:
                lines.append(clean_line)

        return "\n".join(lines)

    def create_standard_format(self, resume_data):
        """Create a standard resume structure."""

        normalized_resume = {}

        for section in self.STANDARD_SECTIONS:
            value = resume_data.get(section, "")

            if isinstance(value, str):
                normalized_resume[section] = (
                    self.normalize_text(value)
                )
            else:
                normalized_resume[section] = value

        return normalized_resume


if __name__ == "__main__":
    normalizer = ResumeNormalizer()

    resume = {
        "summary": """
        Data Analyst with experience in
        Python and SQL.
        """,
        "skills": """
        Python, SQL, Power BI,
        Excel
        """,
        "experience": """
        Data Analyst - ABC Technologies
        """,
        "education": """
        M.Sc Data Science and Analytics
        """,
        "projects": """
        Sales Analytics Dashboard
        """,
        "certifications": """
        Power BI Certification
        """
    }

    result = normalizer.create_standard_format(
        resume
    )

    print("NORMALIZED RESUME:")
    print()

    for section, content in result.items():
        print(f"{section.upper()}:")
        print(content)
        print()