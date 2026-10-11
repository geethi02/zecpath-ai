class ShortlistingEngine:
    """Automatically classify candidates into shortlist,
    review, or reject zones."""

    SHORTLIST_THRESHOLD = 80
    REVIEW_THRESHOLD = 60

    def classify_candidate(self, score):
        """Classify a candidate based on ATS score."""

        if score >= self.SHORTLIST_THRESHOLD:
            return "Shortlist"

        if score >= self.REVIEW_THRESHOLD:
            return "Review"

        return "Reject"

    def shortlist_candidates(self, candidates):
        """Add a shortlisting status to each candidate."""

        results = []

        for candidate in candidates:
            score = candidate.get(
                "candidate_score", 0
            )

            candidate_copy = candidate.copy()

            candidate_copy["status"] = (
                self.classify_candidate(score)
            )

            results.append(candidate_copy)

        return results


if __name__ == "__main__":
    engine = ShortlistingEngine()

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
            "candidate_score": 55.75
        }
    ]

    results = engine.shortlist_candidates(
        candidates
    )

    print("SHORTLISTING RESULTS:")
    print()

    for candidate in results:
        print(
            f"{candidate['name']} - "
            f"{candidate['candidate_score']}% - "
            f"{candidate['status']}"
        )