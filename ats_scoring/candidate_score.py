try:
    from ats_scoring.ats_scorer import ATSScorer
except ModuleNotFoundError:
    from ats_scorer import ATSScorer


class CandidateScoreGenerator:
    """Generate a complete ATS candidate score."""

    def __init__(self, role):

        self.scorer = ATSScorer(role)

    def generate_score(
        self,
        skill_match=None,
        experience_relevance=None,
        education_alignment=None,
        semantic_similarity=None
    ):
        """Generate the final candidate score."""

        result = self.scorer.calculate_score(
            skill_match=skill_match,
            experience_relevance=experience_relevance,
            education_alignment=education_alignment,
            semantic_similarity=semantic_similarity
        )

        return {
            "candidate_score": result[
                "overall_score"
            ],
            "role": result.get(
                "role",
                self.scorer.role
            ),
            "score_breakdown": result[
                "components"
            ],
            "explanation": result[
                "explanation"
            ]
        }


if __name__ == "__main__":

    generator = CandidateScoreGenerator(
        "Data Analyst"
    )

    result = generator.generate_score(
        skill_match=85,
        experience_relevance=75,
        education_alignment=90,
        semantic_similarity=88
    )

    print("CANDIDATE SCORE:")
    print(result)