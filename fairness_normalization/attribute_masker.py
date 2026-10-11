import re


class AttributeMasker:
    """Mask non-essential personal attributes from resumes."""

    PATTERNS = {
        "name": re.compile(
            r"(?im)^\s*(name|candidate name)\s*:\s*.*$"
        ),
        "date_of_birth": re.compile(
            r"(?im)^\s*(date of birth|dob|birth date)\s*:\s*.*$"
        ),
        "gender": re.compile(
            r"(?im)^\s*(gender|sex)\s*:\s*.*$"
        ),
        "address": re.compile(
            r"(?im)^\s*(address|home address|residential address)"
            r"\s*:\s*.*$"
        ),
        "phone": re.compile(
            r"(?i)(\+?\d[\d\s().-]{8,}\d)"
        ),
        "email": re.compile(
            r"(?i)\b[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}\b"
        ),
    }

    def mask_attributes(self, text):
        """Replace non-essential personal information."""

        if not text:
            return ""

        masked_text = text

        masked_text = self.PATTERNS["name"].sub(
            "[NAME MASKED]",
            masked_text
        )

        masked_text = self.PATTERNS["date_of_birth"].sub(
            "[DATE OF BIRTH MASKED]",
            masked_text
        )

        masked_text = self.PATTERNS["gender"].sub(
            "[GENDER MASKED]",
            masked_text
        )

        masked_text = self.PATTERNS["address"].sub(
            "[ADDRESS MASKED]",
            masked_text
        )

        masked_text = self.PATTERNS["phone"].sub(
            "[PHONE MASKED]",
            masked_text
        )

        masked_text = self.PATTERNS["email"].sub(
            "[EMAIL MASKED]",
            masked_text
        )

        return masked_text


if __name__ == "__main__":
    masker = AttributeMasker()

    resume = """
    Name: Ananya Menon
    Email: ananya@example.com
    Phone: +91 9876543210
    Date of Birth: 15/05/2000
    Gender: Female
    Address: Kannur, Kerala

    Skills:
    Python, SQL, Power BI

    Experience:
    Data Analyst at ABC Technologies
    """

    result = masker.mask_attributes(resume)

    print("ORIGINAL RESUME:")
    print(resume)

    print("\nMASKED RESUME:")
    print(result)