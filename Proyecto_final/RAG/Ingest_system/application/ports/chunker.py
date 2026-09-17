from abc import ABC, abstractmethod
from Ingest_system.domain.models.chunk import Chunk


class Chunker(ABC):
    @abstractmethod
    def split(self, text: str, source: str) -> list[Chunk]:
        """Divide el texto de un documento en chunks con overlap."""
        pass