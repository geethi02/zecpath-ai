class ExperienceRelevance:

    def __init__(self):
        self.role_keywords = {
            "data analyst": [
                "data analyst",
                "data analysis",
                "sql",
                "power bi",
                "excel",
                "dashboard",
                "reporting",
            ],
            "data scientist": [
                "data scientist",
                "machine learning",
                "python",
                "statistics",
                "pandas",
                "scikit-learn",
                "data science",
            ],
            "ai engineer": [
                "ai engineer",
                "artificial intelligence",
                "machine learning",
                "python",
                "nlp",
                "genai",
                "llm",
            ],
        }

    def calculate_relevance(
        self,
        job_title,
        required_role,
        experience_text=""
    ):
        """Calculate experience relevance for a target role."""

        job_title = job_title.lower().strip()
        required_role = required_role.lower().strip()
        experience_text = experience_text.lower()

        keywords = self.role_keywords.get(required_role, [])

        if not keywords:
            return {
                "job_title": job_title,
                "required_role": required_role,
                "score": 0,
                "matched_keywords": [],
            }

        matched_keywords = []

        for keyword in keywords:

            if (
                keyword in job_title
                or keyword in experience_text
            ):
                matched_keywords.append(keyword)

        score = (
            len(matched_keywords) / len(keywords)
        ) * 100

        return {
            "job_title": job_title,
            "required_role": required_role,
            "score": round(score, 2),
            "matched_keywords": matched_keywords,
        }


if __name__ == "__main__":

    relevance = ExperienceRelevance()

    experience_text = """
    Data Analyst
    SQL
    Power BI
    Excel
    Dashboard
    Data Analysis
    Reporting
    """

    result = relevance.calculate_relevance(
        job_title="Data Analyst",
        required_role="Data Analyst",
        experience_text=experience_text
    )

    print("EXPERIENCE RELEVANCE:")
    print(result)