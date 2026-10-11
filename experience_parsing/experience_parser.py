import re
from datetime import datetime


class ExperienceParser:
    """Extract and analyze professional experience from resume text."""

    MONTHS = {
        "jan": 1, "january": 1,
        "feb": 2, "february": 2,
        "mar": 3, "march": 3,
        "apr": 4, "april": 4,
        "may": 5,
        "jun": 6, "june": 6,
        "jul": 7, "july": 7,
        "aug": 8, "august": 8,
        "sep": 9, "sept": 9, "september": 9,
        "oct": 10, "october": 10,
        "nov": 11, "november": 11,
        "dec": 12, "december": 12,
    }

    def __init__(self):
        self.experiences = []

    def _parse_date(self, date_text):
        """Convert month-year text into a date."""

        date_text = date_text.strip().lower()

        if date_text in ["present", "current", "now"]:
            return datetime.today().replace(day=1)

        parts = re.split(r"[\s/-]+", date_text)

        if len(parts) != 2:
            return None

        first, second = parts

        if first.isdigit() and len(first) == 4:
            year = int(first)
            month = (
                int(second)
                if second.isdigit()
                else self.MONTHS.get(second)
            )
        else:
            month = self.MONTHS.get(first)
            year = int(second)

        if month and year:
            return datetime(year, month, 1)

        return None

    def _calculate_duration(self, start_date, end_date):
        """Calculate duration in months."""

        if not start_date or not end_date:
            return 0

        months = (
            (end_date.year - start_date.year) * 12
            + (end_date.month - start_date.month)
        )

        return max(months, 0)

    def extract_experience(self, text):
        """Extract company, job title and employment duration."""

        experiences = []

        pattern = re.compile(
            r"(?P<title>[A-Za-z][A-Za-z &/\-]+?)"
            r"\s+(?:at|@|-)\s+"
            r"(?P<company>[A-Za-z0-9 &.,\-]+?)"
            r"\s+"
            r"(?P<start>"
            r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|"
            r"Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|"
            r"Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
            r"[\s/-]+\d{4}"
            r")"
            r"\s*(?:-|to)\s*"
            r"(?P<end>"
            r"(?:Present|Current|Now|"
            r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|"
            r"Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|"
            r"Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
            r"[\s/-]+\d{4})"
            r")",
            re.IGNORECASE,
        )

        for match in pattern.finditer(text):

            title = match.group("title").strip()
            company = match.group("company").strip()

            start_text = match.group("start")
            end_text = match.group("end")

            start_date = self._parse_date(start_text)
            end_date = self._parse_date(end_text)

            duration_months = self._calculate_duration(
                start_date,
                end_date,
            )

            experiences.append(
                {
                    "company": company,
                    "job_title": title,
                    "start_date": start_text,
                    "end_date": end_text,
                    "duration_months": duration_months,
                }
            )

        return experiences

    def calculate_total_experience(self, experiences):
        """Calculate total professional experience in months."""

        total_months = sum(
            experience["duration_months"]
            for experience in experiences
        )

        years = total_months // 12
        months = total_months % 12

        return {
            "total_months": total_months,
            "years": years,
            "months": months,
        }

    def detect_gaps(self, experiences):
        """Detect gaps between employment periods."""

        gaps = []

        sorted_experiences = sorted(
            experiences,
            key=lambda x: self._parse_date(x["start_date"])
        )

        for i in range(len(sorted_experiences) - 1):

            current_end = self._parse_date(
                sorted_experiences[i]["end_date"]
            )

            next_start = self._parse_date(
                sorted_experiences[i + 1]["start_date"]
            )

            if current_end and next_start:

                gap_months = (
                    (next_start.year - current_end.year) * 12
                    + (next_start.month - current_end.month)
                )

                if gap_months > 0:
                    gaps.append(
                        {
                            "from": sorted_experiences[i]["company"],
                            "to": sorted_experiences[i + 1]["company"],
                            "gap_months": gap_months,
                        }
                    )

        return gaps

    def detect_overlaps(self, experiences):
        """Detect overlapping employment periods."""

        overlaps = []

        sorted_experiences = sorted(
            experiences,
            key=lambda x: self._parse_date(x["start_date"])
        )

        for i in range(len(sorted_experiences) - 1):

            current_end = self._parse_date(
                sorted_experiences[i]["end_date"]
            )

            next_start = self._parse_date(
                sorted_experiences[i + 1]["start_date"]
            )

            if current_end and next_start:

                if next_start < current_end:

                    overlap_months = (
                        (current_end.year - next_start.year) * 12
                        + (current_end.month - next_start.month)
                    )

                    overlaps.append(
                        {
                            "company_1": sorted_experiences[i]["company"],
                            "company_2": sorted_experiences[i + 1]["company"],
                            "overlap_months": overlap_months,
                        }
                    )

        return overlaps


if __name__ == "__main__":

    parser = ExperienceParser()

    sample_resume = """
    Data Analyst at ABC Technologies
    January 2024 - December 2025

    Data Science Intern at XYZ Solutions
    Jun 2023 - Dec 2023

    AI Engineer at Tech Solutions
    Jan 2026 - Present
    """

    result = parser.extract_experience(sample_resume)

    print("EXPERIENCES:")

    for experience in result:
        print(experience)

    total_experience = parser.calculate_total_experience(result)

    print("\nTOTAL EXPERIENCE:")
    print(total_experience)

    gaps = parser.detect_gaps(result)

    print("\nEXPERIENCE GAPS:")
    print(gaps)

    overlaps = parser.detect_overlaps(result)

    print("\nEXPERIENCE OVERLAPS:")
    print(overlaps)