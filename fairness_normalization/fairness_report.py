try:
    from fairness_normalization.resume_normalizer import ResumeNormalizer
    from fairness_normalization.attribute_masker import AttributeMasker
    from fairness_normalization.bias_evaluator import BiasEvaluator
except ModuleNotFoundError:
    from resume_normalizer import ResumeNormalizer
    from attribute_masker import AttributeMasker
    from bias_evaluator import BiasEvaluator


class FairnessReport:
    """Generate a fairness and normalization report."""

    def __init__(self):
        self.normalizer = ResumeNormalizer()
        self.masker = AttributeMasker()
        self.bias_evaluator = BiasEvaluator()

    def generate_report(self, resume_data):
        """Generate a fairness evaluation report."""

        standard_resume = (
            self.normalizer.create_standard_format(
                resume_data
            )
        )

        full_text = "\n".join(
            str(value)
            for value in standard_resume.values()
        )

        bias_result = self.bias_evaluator.evaluate(
            full_text
        )

        masked_text = self.masker.mask_attributes(
            full_text
        )

        return {
            "standardized": True,
            "bias_indicators": bias_result[
                "indicators"
            ],
            "masking_recommended": bias_result[
                "masking_recommended"
            ],
            "masked_resume_available": bool(
                masked_text
            ),
        }


if __name__ == "__main__":
    resume_data = {
        "summary": """
        Name: Ananya Menon
        Data Analyst with experience in Python and SQL.
        """,
        "skills": """
        Python, SQL, Power BI, Excel
        """,
        "experience": """
        Data Analyst at ABC Technologies
        """,
        "education": """
        M.Sc Data Science and Analytics
        """,
        "projects": """
        Sales Analytics Dashboard
        """,
        "certifications": """
        Power BI Certification
        """
    }

    report_generator = FairnessReport()

    report = report_generator.generate_report(
        resume_data
    )

    print("FAIRNESS & NORMALIZATION REPORT:")
    print()

    for key, value in report.items():
        print(f"{key}: {value}")