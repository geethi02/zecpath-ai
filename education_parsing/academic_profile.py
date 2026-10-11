from education_parser import EducationParser


class AcademicProfile:

    def __init__(self):
        self.parser = EducationParser()

    def build_profile(self, resume_text):

        education = self.parser.extract_education(
            resume_text
        )

        certifications = self.parser.extract_certifications(
            resume_text
        )

        return {
            "education": education,
            "certifications": certifications,
            "total_degrees": len(education),
            "total_certifications": len(certifications),
        }


if __name__ == "__main__":

    resume_text = """
    M.Sc Data Science and Analytics
    Jain University, Bangalore
    2026

    B.Sc Mathematics
    Kannur University
    2024

    Microsoft Certified Power BI Data Analyst
    AWS Certified Cloud Practitioner
    """

    profile = AcademicProfile()

    result = profile.build_profile(
        resume_text
    )

    print("\nSTRUCTURED ACADEMIC PROFILE:")
    print(result)