class ScoringConfig:
    """Configurable ATS scoring weights."""

    DEFAULT_WEIGHTS = {
        "skill_match": 35,
        "experience_relevance": 25,
        "education_alignment": 15,
        "semantic_similarity": 25,
    }

    ROLE_WEIGHTS = {

        "data analyst": {
            "skill_match": 40,
            "experience_relevance": 25,
            "education_alignment": 15,
            "semantic_similarity": 20,
        },

        "data scientist": {
            "skill_match": 35,
            "experience_relevance": 25,
            "education_alignment": 15,
            "semantic_similarity": 25,
        },

        "ai engineer": {
            "skill_match": 35,
            "experience_relevance": 20,
            "education_alignment": 10,
            "semantic_similarity": 35,
        },
    }

    @classmethod
    def get_weights(cls, role):
        """Return weights for a specific role."""

        role = role.lower().strip()

        weights = cls.ROLE_WEIGHTS.get(
            role,
            cls.DEFAULT_WEIGHTS
        )

        return weights.copy()


if __name__ == "__main__":

    print("DEFAULT WEIGHTS:")
    print(ScoringConfig.DEFAULT_WEIGHTS)

    print("\nDATA ANALYST WEIGHTS:")
    print(
        ScoringConfig.get_weights(
            "Data Analyst"
        )
    )

    print("\nAI ENGINEER WEIGHTS:")
    print(
        ScoringConfig.get_weights(
            "AI Engineer"
        )
    )