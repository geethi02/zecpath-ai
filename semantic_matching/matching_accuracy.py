from semantic_matcher import SemanticMatcher


class MatchingAccuracy:

    def __init__(self):

        self.matcher = SemanticMatcher()

    def run_validation(self):

        test_cases = [

            {
                "job_type": "Data Analyst",
                "resume": """
                Data Analyst with experience in Python,
                SQL, Power BI, Excel and dashboards.
                """,
                "job_description": """
                Looking for a Data Analyst with Python,
                SQL, Power BI, Excel and reporting skills.
                """
            },

            {
                "job_type": "Data Scientist",
                "resume": """
                Data Scientist with experience in Python,
                machine learning, statistics, Pandas
                and scikit-learn.
                """,
                "job_description": """
                Looking for a Data Scientist with strong
                Python, machine learning, statistics
                and predictive modeling skills.
                """
            },

            {
                "job_type": "AI Engineer",
                "resume": """
                AI Engineer experienced in Python,
                machine learning, NLP, LLMs and
                Generative AI applications.
                """,
                "job_description": """
                Looking for an AI Engineer with experience
                in Python, machine learning, NLP,
                LLM and Generative AI systems.
                """
            },

            {
                "job_type": "Marketing Specialist",
                "resume": """
                Marketing professional with experience
                in social media campaigns, branding,
                content creation and digital marketing.
                """,
                "job_description": """
                Looking for a marketing specialist with
                experience in social media, branding,
                advertising and content strategy.
                """
            }
        ]

        results = []

        for test_case in test_cases:

            result = self.matcher.match_resume_to_job(
                test_case["resume"],
                test_case["job_description"]
            )

            results.append(
                {
                    "job_type": test_case["job_type"],
                    "similarity_score": result[
                        "similarity_score"
                    ],
                    "match_level": result[
                        "match_level"
                    ]
                }
            )

        return results


if __name__ == "__main__":

    validator = MatchingAccuracy()

    results = validator.run_validation()

    print("MATCHING ACCURACY REPORT:")
    print()

    for result in results:

        print(
            f"{result['job_type']}: "
            f"{result['similarity_score']}% "
            f"- {result['match_level']}"
        )
        