from sentence_transformers import util


class SimilarityScorer:
    """Calculate semantic similarity between text embeddings."""

    def calculate_similarity(
        self,
        embedding_a,
        embedding_b
    ):
        """Calculate cosine similarity."""

        if embedding_a is None or embedding_b is None:
            return 0.0

        similarity = util.cos_sim(
            embedding_a,
            embedding_b
        )

        return round(
            float(similarity[0][0]) * 100,
            2
        )


if __name__ == "__main__":

    from embedding_engine import EmbeddingEngine

    engine = EmbeddingEngine()
    scorer = SimilarityScorer()

    resume_text = """
    Data Analyst with experience in Python,
    SQL, Power BI and data visualization.
    """

    job_description = """
    We are looking for a Data Analyst with
    strong Python, SQL, Power BI and
    dashboard development skills.
    """

    resume_embedding = engine.generate_embedding(
        resume_text
    )

    jd_embedding = engine.generate_embedding(
        job_description
    )

    score = scorer.calculate_similarity(
        resume_embedding,
        jd_embedding
    )

    print("SEMANTIC SIMILARITY SCORE:")
    print(f"{score}%")