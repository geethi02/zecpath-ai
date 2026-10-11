import re


class EducationParser:
    """Extract academic qualifications and certifications from resumes."""

    DEGREE_NORMALIZATION = {
        "b.sc": "Bachelor of Science",
        "bsc": "Bachelor of Science",
        "m.sc": "Master of Science",
        "msc": "Master of Science",
        "b.tech": "Bachelor of Technology",
        "btech": "Bachelor of Technology",
        "m.tech": "Master of Technology",
        "mtech": "Master of Technology",
        "b.e": "Bachelor of Engineering",
        "be": "Bachelor of Engineering",
        "m.e": "Master of Engineering",
        "me": "Master of Engineering",
        "bca": "Bachelor of Computer Applications",
        "mca": "Master of Computer Applications",
        "b.com": "Bachelor of Commerce",
        "m.com": "Master of Commerce",
        "phd": "PhD",
        "ph.d": "PhD",
    }

    CERTIFICATION_KEYWORDS = [
        "certified",
        "certification",
        "certificate",
        "aws certified",
        "azure",
        "google cloud",
        "microsoft certified",
        "power bi",
        "tableau",
        "python certification",
        "sql certification",
    ]

    def normalize_degree(self, degree):
        """Normalize degree naming."""

        key = degree.lower().strip()

        return self.DEGREE_NORMALIZATION.get(
            key,
            degree.strip()
        )

    def extract_education(self, text):
        """Extract degree, field, institution and graduation year."""

        education = []

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        degree_pattern = re.compile(
            r"^(?P<degree>"
            r"B\.?Sc|M\.?Sc|B\.?Tech|M\.?Tech|"
            r"B\.?E|M\.?E|BCA|MCA|B\.?Com|M\.?Com|"
            r"Ph\.?D"
            r")"
            r"(?:\s+in\s+|\s+)"
            r"(?P<field>[A-Za-z][A-Za-z &/.-]*)$",
            re.IGNORECASE,
        )

        for i, line in enumerate(lines):

            match = degree_pattern.match(line)

            if not match:
                continue

            degree = match.group("degree")
            field = match.group("field").strip()

            institution = None
            graduation_year = None

            following_lines = lines[i + 1:i + 3]

            for next_line in following_lines:

                year_match = re.search(
                    r"\b(19|20)\d{2}\b",
                    next_line
                )

                if year_match:
                    graduation_year = int(
                        year_match.group(0)
                    )

                if not re.fullmatch(
                    r"(19|20)\d{2}",
                    next_line
                ):
                    if institution is None:
                        institution = next_line

            education.append(
                {
                    "degree_type": self.normalize_degree(
                        degree
                    ),
                    "field_of_study": field,
                    "institution": institution,
                    "graduation_year": graduation_year,
                }
            )

        return education

    def extract_certifications(self, text):
        """Extract certifications and categorize them."""

        certifications = []

        for line in text.splitlines():

            clean_line = line.strip()

            if not clean_line:
                continue

            lower_line = clean_line.lower()

            for keyword in self.CERTIFICATION_KEYWORDS:

                if keyword in lower_line:

                    certifications.append(
                        {
                            "name": clean_line,
                            "category": self.categorize_certification(
                                clean_line
                            ),
                        }
                    )

                    break

        return certifications

    def categorize_certification(self, certification):
        """Assign a relevance category."""

        certification = certification.lower()

        if any(
            keyword in certification
            for keyword in [
                "aws",
                "azure",
                "google cloud",
                "cloud",
            ]
        ):
            return "Cloud"

        if any(
            keyword in certification
            for keyword in [
                "machine learning",
                "artificial intelligence",
                " ai ",
            ]
        ):
            return "AI & Machine Learning"

        if any(
            keyword in certification
            for keyword in [
                "power bi",
                "tableau",
                "data",
                "sql",
                "python",
            ]
        ):
            return "Data & Analytics"

        return "General"


if __name__ == "__main__":

    parser = EducationParser()

    sample_resume = """
    M.Sc Data Science and Analytics
    Jain University, Bangalore
    2026

    B.Sc Mathematics
    Kannur University
    2024

    Microsoft Certified Power BI Data Analyst
    AWS Certified Cloud Practitioner
    """

    education = parser.extract_education(
        sample_resume
    )

    certifications = parser.extract_certifications(
        sample_resume
    )

    print("EDUCATION:")

    for item in education:
        print(item)

    print("\nCERTIFICATIONS:")

    for certification in certifications:
        print(certification)