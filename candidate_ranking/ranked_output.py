from ranking_engine import CandidateRankingEngine
from shortlisting import ShortlistingEngine


class RankedCandidateOutput:
    """Generate recruiter-friendly ranked candidate output."""

    def __init__(self):
        self.ranking_engine = CandidateRankingEngine()
        self.shortlisting_engine = ShortlistingEngine()

    def generate_output(self, candidates):
        """Rank and classify candidates."""

        ranked_candidates = self.ranking_engine.rank_candidates(
            candidates
        )

        final_output = (
            self.shortlisting_engine.shortlist_candidates(
                ranked_candidates
            )
        )

        return final_output

    def print_output(self, candidates):
        """Print a recruiter-friendly candidate list."""

        print("RANKED CANDIDATE OUTPUT")
        print("=" * 60)

        for candidate in candidates:
            print(
                f"Rank: {candidate['rank']} | "
                f"ID: {candidate['candidate_id']} | "
                f"Name: {candidate['name']} | "
                f"Score: {candidate['candidate_score']}% | "
                f"Status: {candidate['status']}"
            )


if __name__ == "__main__":
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

    output_generator = RankedCandidateOutput()

    results = output_generator.generate_output(
        candidates
    )

    output_generator.print_output(results)