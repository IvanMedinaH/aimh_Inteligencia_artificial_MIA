from abc import ABC, abstractmethod

class PDFConverter(ABC):
    @abstractmethod
    def convert_to_md(self, pdf_path: str, output_path: str) -> str:
        """
        Lee un archivo PDF, extrae su texto y lo guarda como un archivo .md.
        Devuelve la ruta del archivo generado.
        """
        pass