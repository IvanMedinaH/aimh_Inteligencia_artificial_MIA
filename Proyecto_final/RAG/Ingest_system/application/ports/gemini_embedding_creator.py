from abc import ABC, abstractmethod
from typing import List

class GeminiEmbeddingCreator(ABC):
    @abstractmethod
    def create_embedding(self, text: str) -> List[float]:
        pass

    @abstractmethod
    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        pass