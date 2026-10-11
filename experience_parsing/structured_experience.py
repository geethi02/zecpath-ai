from experience_parser import ExperienceParser
from experience_relevance import ExperienceRelevance


class StructuredExperience:

    def __init__(self):
        self.parser = ExperienceParser()
        self.relevance = ExperienceRelevance()

    def build_experience_object(
        self,
        resume_text,
        target_role
    ):
        """Build complete structured experience object."""

        experiences = self.parser.extract_experience(
            resume_text
        )

        total_experience = (
            self.parser.calculate_total_experience(
                experiences
            )
        )

        gaps = self.parser.detect_gaps(
            experiences
        )

        overlaps = self.parser.detect_overlaps(
            experiences
        )

        relevance_results = []

        for experience in experiences:

            experience_text = (
                experience["job_title"]
                + " "
                + experience["company"]
            )

            relevance = (
                self.relevance.calculate_relevance(
                    job_title=experience["job_title"],
                    required_role=target_role,
                    experience_text=experience_text
                )
            )

            relevance_results.append(relevance)

        return {
            "experiences": experiences,
            "total_experience": total_experience,
            "gaps": gaps,
            "overlaps": overlaps,
            "relevance": relevance_results,
        }


if __name__ == "__main__":

    resume_text = """
    Data Analyst at ABC Technologies
    January 2024 - December 2025

    Data Science Intern at XYZ Solutions
    Jun 2023 - Dec 2023

    AI Engineer at Tech Solutions
    Jan 2026 - Present
    """

    processor = StructuredExperience()

    result = processor.build_experience_object(
        resume_text,
        "Data Analyst"
    )

    print("\nSTRUCTURED EXPERIENCE OBJECT:")
    print(result)