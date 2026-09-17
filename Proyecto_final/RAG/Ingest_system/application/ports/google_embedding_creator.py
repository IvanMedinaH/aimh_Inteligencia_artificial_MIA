from abc import ABC, abstractmethod
from typing import List

class GoogleEmbeddingCreator(ABC):
    @abstractmethod
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Genera una lista de embeddings para una lista de textos (chunks)."""
        pass

    @abstractmethod
    def embed_query(self, text: str) -> list[float]:
        """Genera el vector de una consulta individual."""
        pass