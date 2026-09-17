from abc import ABC, abstractmethod
from Ingest_system.domain.models.document import Document

class DocumentLoader(ABC):
    @abstractmethod
    def load(self, file_path: str) -> Document:
        """Lee un archivo de disco y lo convierte en un Documento del dominio."""
        pass