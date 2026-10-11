class BiasEvaluator:
    """Evaluate resumes for potential bias indicators."""

    SENSITIVE_ATTRIBUTES = [
        "name",
        "gender",
        "sex",
        "date of birth",
        "dob",
        "age",
        "marital status",
        "religion",
        "nationality",
        "photo",
        "address",
        "phone",
        "email",
    ]

    def find_bias_indicators(self, text):
        """Find potentially non-essential personal attributes."""

        if not text:
            return []

        text_lower = text.lower()
        indicators = []

        for attribute in self.SENSITIVE_ATTRIBUTES:
            if attribute in text_lower:
                indicators.append(attribute)

        return indicators

    def evaluate(self, text):
        """Generate a simple bias-indicator report."""

        indicators = self.find_bias_indicators(text)

        return {
            "bias_indicators_found": len(indicators),
            "indicators": indicators,
            "masking_recommended": len(indicators) > 0,
        }


if __name__ == "__main__":
    evaluator = BiasEvaluator()

    resume = """
    Name: Ananya Menon
    Gender: Female
    Date of Birth: 15/05/2000
    Address: Kannur, Kerala

    Skills:
    Python, SQL, Power BI

    Experience:
    Data Analyst
    """

    result = evaluator.evaluate(resume)

    print("BIAS INDICATOR REPORT:")
    print(result)