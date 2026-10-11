class CandidateRankingEngine:
    """Rank candidates based on ATS scores."""

    def rank_candidates(self, candidates):
        """Sort candidates from highest score to lowest score."""

        ranked_candidates = sorted(
            candidates,
            key=lambda candidate: candidate.get(
                "candidate_score", 0
            ),
            reverse=True
        )

        for index, candidate in enumerate(
            ranked_candidates,
            start=1
        ):
            candidate["rank"] = index

        return ranked_candidates


if __name__ == "__main__":
    engine = CandidateRankingEngine()

    candidates = [
        {
            "candidate_id": "C001",
            "name": "Ananya",
            "candidate_score": 83.85
        },
        {
            "candidate_id": "C002",
            "name": "Rahul",
            "candidate_score": 72.40
        },
        {
            "candidate_id": "C003",
            "name": "Meera",
            "candidate_score": 91.20
        },
        {
            "candidate_id": "C004",
            "name": "Arjun",
            "candidate_score": 65.75
        }
    ]

    ranked_candidates = engine.rank_candidates(
        candidates
    )

    print("RANKED CANDIDATES:")
    print()

    for candidate in ranked_candidates:
        print(
            f"Rank {candidate['rank']}: "
            f"{candidate['name']} - "
            f"{candidate['candidate_score']}%"
        )