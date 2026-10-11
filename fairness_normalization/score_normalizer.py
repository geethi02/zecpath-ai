class ScoreNormalizer:
    """Normalize candidate scores to a 0-100 scale."""

    def normalize_score(self, score, minimum=0, maximum=100):
        """Convert a score to a standard 0-100 range."""

        if score is None:
            return 0.0

        if maximum <= minimum:
            return 0.0

        normalized_score = (
            (score - minimum)
            / (maximum - minimum)
        ) * 100

        normalized_score = max(
            0,
            min(100, normalized_score)
        )

        return round(normalized_score, 2)

    def normalize_scores(self, scores):
        """Normalize a list of candidate scores."""

        if not scores:
            return []

        minimum = min(scores)
        maximum = max(scores)

        return [
            self.normalize_score(
                score,
                minimum,
                maximum
            )
            for score in scores
        ]


if __name__ == "__main__":
    normalizer = ScoreNormalizer()

    scores = [65, 72, 80, 91, 95]

    normalized_scores = normalizer.normalize_scores(
        scores
    )

    print("ORIGINAL SCORES:")
    print(scores)

    print("\nNORMALIZED SCORES:")
    print(normalized_scores)