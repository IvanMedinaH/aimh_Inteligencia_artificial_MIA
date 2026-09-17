import os
from google import genai
from Ingest_system.application.ports.google_embedding_creator import GoogleEmbeddingCreator

class GoogleGoogleEmbeddingService(GoogleEmbeddingCreator):
    def __init__(self, model_name: str = "text-embedding-004"):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY no configurada en el entorno.")
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        response = self.client.models.embed_content(
            model=self.model_name,
            contents=texts
        )
        return [e.values for e in response.embeddings]

    def embed_query(self, text: str) -> list[float]:
        return self.embed_texts([text])[0]