from abc import ABC, abstractmethod
from Ingest_system.domain.models.chunk import Chunk

class VectorStore(ABC):
    @abstractmethod
    def save_chunks(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        """Persiste los chunks y sus vectores en ChromaDB."""
        pass

    @abstractmethod
    def search_similar(self, query_embedding: list[float], top_k: int = 3) -> list[Chunk]:
        """Recupera los K chunks más similares al vector de consulta."""
        pass