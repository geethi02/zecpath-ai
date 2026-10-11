from sentence_transformers import SentenceTransformer


class EmbeddingEngine:
    """Convert text into semantic embeddings."""

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def generate_embedding(self, text):
        """Generate an embedding for a single text."""

        if not text or not text.strip():
            return None

        embedding = self.model.encode(
            text,
            convert_to_tensor=False
        )

        return embedding

    def generate_embeddings(self, texts):
        """Generate embeddings for multiple texts."""

        if not texts:
            return []

        embeddings = self.model.encode(
            texts,
            convert_to_tensor=False
        )

        return embeddings


if __name__ == "__main__":

    engine = EmbeddingEngine()

    sample_text = """
    Data Analyst with experience in Python,
    SQL, Power BI and data visualization.
    """

    embedding = engine.generate_embedding(
        sample_text
    )

    print("EMBEDDING GENERATED")
    print("Embedding dimensions:", len(embedding))
    print("First 5 values:", embedding[:5])