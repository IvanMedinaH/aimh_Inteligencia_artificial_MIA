import os
from typing import List
from google import genai
from Ingest_system.application.ports.gemini_embedding_creator import GeminiEmbeddingCreator


class GeminiEmbeddingService(GeminiEmbeddingCreator):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY no está configurada")

        self.client = genai.Client(api_key=self.api_key)
        self.model_name = "gemini-embedding-001"

    def create_embedding(self, text: str) -> List[float]:
        """Genera el embedding para un texto individual."""
        response = self.client.models.embed_content(
            model=self.model_name,
            contents=text,
        )

        # Guard clause para asegurar el tipado
        if not response.embeddings or len(response.embeddings) == 0:
            raise ValueError("La respuesta de la API no contiene embeddings válidos.")

        values = response.embeddings[0].values
        if values is None:
            raise ValueError("El vector de embeddings devuelto por la API es nulo.")

        return list(values)

    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Genera embeddings por lotes de forma eficiente en una sola llamada."""
        if not texts:
            return []

        response = self.client.models.embed_content(
            model=self.model_name,
            contents=texts,
        )

        if not response.embeddings:
            raise ValueError("La respuesta de la API no contiene embeddings válidos.")

        # Garantizamos al linter que response.embeddings es una lista no nula
        embeddings_list: List[List[float]] = []
        for emb in response.embeddings:
            if emb.values is not None:
                embeddings_list.append(list(emb.values))

        return embeddings_list