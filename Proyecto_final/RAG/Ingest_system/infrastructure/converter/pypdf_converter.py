from pathlib import Path
import pypdfium2 as pdfium
import numpy as np
from Ingest_system.application.ports.pdf_converter import PDFConverter


class PyPDFConverter(PDFConverter):
    def __init__(self):
        self._ocr_reader = None

    def _get_ocr_reader(self):
        if self._ocr_reader is None:
            import easyocr
            # Inicializar EasyOCR en español e inglés
            print("⏳ Cargando modelo EasyOCR (solo la primera vez)...")
            self._ocr_reader = easyocr.Reader(['es', 'en'], gpu=False)
        return self._ocr_reader

    def convert_to_md(self, pdf_path: str, output_path: str = None) -> str:
        source_path = Path(pdf_path).resolve()

        if not source_path.exists():
            raise FileNotFoundError(f"El archivo PDF no existe: {source_path}")

        if output_path is None:
            output_path = source_path.with_suffix(".md")
        else:
            output_path = Path(output_path).resolve()

        pdf = pdfium.PdfDocument(source_path)
        extracted_text = []

        for i, page in enumerate(pdf):
            text_page = page.get_textpage()
            text = text_page.get_text_range().replace("\x00", "").strip()

            # Si el PDF tiene texto digital tradicional
            if len(text) > 0:
                extracted_text.append(f"\n{text}")
            else:
                # Si el texto es vectorial/imagen (0 caracteres), aplicar OCR
                print(f"🔍 Pagina {i + 1} de {source_path.name} sin texto vectorial. Aplicando OCR...")
                pil_image = page.render(scale=2).to_pil()
                reader = self._get_ocr_reader()
                ocr_results = reader.readtext(np.array(pil_image), detail=0)
                ocr_text = "\n".join(ocr_results)

                if ocr_text.strip():
                    extracted_text.append(f"\n{ocr_text.strip()}")

        full_content = "\n\n".join(
            extracted_text) if extracted_text else f"# {source_path.stem}\n\n[Sin texto extraíble]"

        with open(output_path, "w", encoding="utf-8", errors="ignore") as f:
            f.write(full_content)

        return str(output_path)


def process_data_folder():
    # Detecta la ruta absoluta de este script
    current_path = Path(__file__).resolve()

    # Sube por el árbol de directorios hasta encontrar la carpeta 'Ingest_system'
    ingest_system_dir = None
    for parent in [current_path] + list(current_path.parents):
        if parent.name == "Ingest_system":
            ingest_system_dir = parent
            break

    # Si no la encuentra por nombre, usa la carpeta 'data' directamente si existe cerca
    if ingest_system_dir:
        data_dir = ingest_system_dir / "data"
    else:
        # Fallback estándar
        data_dir = current_path.parent / "data"

    print(f"📂 Buscando PDFs en la ruta correcta: {data_dir}")

    if not data_dir.exists():
        print(f"❌ La carpeta no existe: {data_dir}")
        return

    converter = PyPDFConverter()
    pdf_files = list(data_dir.glob("*.pdf"))

    print(f"📄 PDFs encontrados: {len(pdf_files)}")

    for pdf in pdf_files:
        md_file = converter.convert_to_md(str(pdf))
        print(f"✅ Convertido con éxito: {pdf.name} -> {Path(md_file).name}")


if __name__ == "__main__":
    process_data_folder()