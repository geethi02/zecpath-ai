class EducationRelevance:

    def __init__(self):

        self.role_requirements = {

            "data analyst": {
                "degrees": [
                    "data science",
                    "data analytics",
                    "computer science",
                    "statistics",
                    "mathematics",
                    "information technology",
                ],
                "certifications": [
                    "power bi",
                    "tableau",
                    "sql",
                    "data analytics",
                    "python",
                ],
            },

            "data scientist": {
                "degrees": [
                    "data science",
                    "data analytics",
                    "computer science",
                    "statistics",
                    "mathematics",
                ],
                "certifications": [
                    "machine learning",
                    "artificial intelligence",
                    "python",
                    "data science",
                ],
            },

            "ai engineer": {
                "degrees": [
                    "artificial intelligence",
                    "computer science",
                    "data science",
                    "machine learning",
                ],
                "certifications": [
                    "artificial intelligence",
                    "machine learning",
                    "python",
                    "cloud",
                ],
            },
        }

    def calculate_relevance(
        self,
        education,
        certifications,
        target_role
    ):
        """Calculate education relevance for a target role."""

        target_role = target_role.lower().strip()

        requirements = self.role_requirements.get(
            target_role
        )

        if not requirements:
            return {
                "target_role": target_role,
                "score": 0,
                "matched_degrees": [],
                "matched_certifications": [],
            }

        matched_degrees = []
        matched_certifications = []

        degree_keywords = requirements["degrees"]
        certification_keywords = requirements["certifications"]

        for item in education:

            field = (
                item.get("field_of_study") or ""
            ).lower()

            degree_type = (
                item.get("degree_type") or ""
            ).lower()

            education_text = (
                field + " " + degree_type
            )

            for keyword in degree_keywords:

                if keyword in education_text:
                    if keyword not in matched_degrees:
                        matched_degrees.append(keyword)

        for item in certifications:

            certification_name = (
                item.get("name") or ""
            ).lower()

            certification_category = (
                item.get("category") or ""
            ).lower()

            certification_text = (
                certification_name
                + " "
                + certification_category
            )

            for keyword in certification_keywords:

                if keyword in certification_text:
                    if keyword not in matched_certifications:
                        matched_certifications.append(keyword)

        degree_score = 0

        if degree_keywords:

            degree_score = (
                len(matched_degrees)
                / len(degree_keywords)
            ) * 70

        certification_score = 0

        if certification_keywords:

            certification_score = (
                len(matched_certifications)
                / len(certification_keywords)
            ) * 30

        final_score = (
            degree_score
            + certification_score
        )

        return {
            "target_role": target_role,
            "score": round(final_score, 2),
            "matched_degrees": matched_degrees,
            "matched_certifications": matched_certifications,
        }


if __name__ == "__main__":

    relevance = EducationRelevance()

    education = [
        {
            "degree_type": "Master of Science",
            "field_of_study": "Data Science and Analytics",
            "institution": "Jain University",
            "graduation_year": 2026,
        },
        {
            "degree_type": "Bachelor of Science",
            "field_of_study": "Mathematics",
            "institution": "Kannur University",
            "graduation_year": 2024,
        },
    ]

    certifications = [
        {
            "name": "Microsoft Certified Power BI Data Analyst",
            "category": "Data & Analytics",
        },
        {
            "name": "AWS Certified Cloud Practitioner",
            "category": "Cloud",
        },
    ]

    result = relevance.calculate_relevance(
        education,
        certifications,
        "Data Analyst"
    )

    print("EDUCATION RELEVANCE:")
    print(result)