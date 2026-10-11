from embedding_engine import EmbeddingEngine
from similarity_scorer import SimilarityScorer


class SemanticMatcher:
    """Match resumes with job descriptions semantically."""

    def __init__(self):

        self.embedding_engine = EmbeddingEngine()
        self.similarity_scorer = SimilarityScorer()

    def match_resume_to_job(
        self,
        resume_text,
        job_description
    ):
        """Calculate resume-to-JD semantic similarity."""

        resume_embedding = (
            self.embedding_engine.generate_embedding(
                resume_text
            )
        )

        jd_embedding = (
            self.embedding_engine.generate_embedding(
                job_description
            )
        )

        similarity_score = (
            self.similarity_scorer.calculate_similarity(
                resume_embedding,
                jd_embedding
            )
        )

        return {
            "similarity_score": similarity_score,
            "match_level": self.get_match_level(
                similarity_score
            ),
        }

    def get_match_level(self, score):
        """Classify semantic similarity."""

        if score >= 80:
            return "Very Strong Match"

        if score >= 65:
            return "Strong Match"

        if score >= 50:
            return "Moderate Match"

        if score >= 35:
            return "Weak Match"

        return "Low Match"


if __name__ == "__main__":

    matcher = SemanticMatcher()

    resume_text = """
    Data Analyst with experience in Python,
    SQL, Power BI, Excel and data visualization.
    """

    job_description = """
    We are looking for a Data Analyst with
    strong Python, SQL, Power BI and
    dashboard development skills.
    """

    result = matcher.match_resume_to_job(
        resume_text,
        job_description
    )

    print("SEMANTIC RESUME-JD MATCH:")
    print(result)