class SimilarityThresholds:
    """Define semantic matching thresholds."""

    VERY_STRONG = 80
    STRONG = 65
    MODERATE = 50
    WEAK = 35

    @classmethod
    def classify(cls, score):

        if score >= cls.VERY_STRONG:
            return "Very Strong Match"

        if score >= cls.STRONG:
            return "Strong Match"

        if score >= cls.MODERATE:
            return "Moderate Match"

        if score >= cls.WEAK:
            return "Weak Match"

        return "Low Match"


if __name__ == "__main__":

    test_scores = [
        90,
        75,
        55,
        40,
        20
    ]

    print("SIMILARITY THRESHOLD TEST:")

    for score in test_scores:

        print(
            f"{score}% -> "
            f"{SimilarityThresholds.classify(score)}"
        )