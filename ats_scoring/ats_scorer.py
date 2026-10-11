try:
    from ats_scoring.scoring_config import ScoringConfig
except ModuleNotFoundError:
    from scoring_config import ScoringConfig


class ATSScorer:
    """Calculate an explainable ATS candidate score."""

    def __init__(self, role):

        self.role = role
        self.weights = ScoringConfig.get_weights(role)

    def calculate_score(
        self,
        skill_match=None,
        experience_relevance=None,
        education_alignment=None,
        semantic_similarity=None
    ):
        """Calculate weighted candidate score."""

        components = {
            "skill_match": skill_match,
            "experience_relevance": experience_relevance,
            "education_alignment": education_alignment,
            "semantic_similarity": semantic_similarity,
        }

        available_components = {
            key: value
            for key, value in components.items()
            if value is not None
        }

        if not available_components:

            return {
                "overall_score": 0,
                "components": {},
                "explanation": "No scoring data available."
            }

        total_weight = sum(
            self.weights[key]
            for key in available_components
        )

        weighted_score = 0

        component_details = {}

        for key, value in available_components.items():

            weight = self.weights[key]

            contribution = (
                value * weight / total_weight
            )

            weighted_score += contribution

            component_details[key] = {
                "score": value,
                "weight": weight,
                "contribution": round(
                    contribution,
                    2
                )
            }

        overall_score = round(
            weighted_score,
            2
        )

        return {
            "role": self.role,
            "overall_score": overall_score,
            "components": component_details,
            "explanation": self.generate_explanation(
                component_details
            )
        }

    def generate_explanation(
        self,
        component_details
    ):
        """Generate a human-readable explanation."""

        explanations = []

        for key, details in component_details.items():

            explanations.append(
                f"{key}: "
                f"{details['score']}% "
                f"(weight {details['weight']}%)"
            )

        return "; ".join(explanations)


if __name__ == "__main__":

    scorer = ATSScorer(
        "Data Analyst"
    )

    result = scorer.calculate_score(
        skill_match=85,
        experience_relevance=75,
        education_alignment=90,
        semantic_similarity=88
    )

    print("ATS SCORE:")
    print(result)