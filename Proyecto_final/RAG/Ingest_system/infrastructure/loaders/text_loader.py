from pathlib import Path
from typing import Dict, Any
from Ingest_system.domain.models.document import Document
from Ingest_system.application.ports.document_loader import DocumentLoader

class TextLoader(DocumentLoader):
    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        # Resolver ruta relativa desde la raíz del proyecto
        if not path.is_absolute():
            # Sube desde 'infrastructure/loaders' (4 niveles) hasta la raíz
            PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
            path = (PROJECT_ROOT / path).resolve()

        if not path.exists():
            raise FileNotFoundError(f"El archivo no existe en la ruta: {path}")

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Instanciación correcta con tu @dataclass
        return Document(
            id=path.name,
            content=content,
            source=str(path),
            metadata={"filename": path.name, "extension": path.suffix}
        )