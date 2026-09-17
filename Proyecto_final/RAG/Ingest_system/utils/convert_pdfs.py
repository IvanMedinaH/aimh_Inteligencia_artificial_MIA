from pathlib import Path
from Ingest_system.infrastructure.converter.pypdf_converter import PyPDFConverter


def process_data_folder():
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_dir = BASE_DIR / "Ingest_system" / "data"

    print(f"📂 Buscando PDFs en: {data_dir}")

    if not data_dir.exists():
        print(f"❌ La carpeta {data_dir} no existe.")
        return

    converter = PyPDFConverter()
    pdf_files = list(data_dir.glob("*.pdf"))

    print(f"📄 Encontrados {len(pdf_files)} archivos PDF para convertir...")

    for pdf in pdf_files:
        md_file = converter.convert_to_md(str(pdf))
        print(f"✅ Convertido exitosamente: {pdf.name} -> {Path(md_file).name}")


if __name__ == "__main__":
    process_data_folder()