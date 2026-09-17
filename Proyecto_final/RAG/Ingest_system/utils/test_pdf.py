from pathlib import Path
import pypdfium2 as pdfium

# Subir 2 niveles desde utils/ para llegar a Ingest_system/
# Path(__file__) = Ingest_system/utils/test_pdf.py
# .parent        = Ingest_system/utils/
# .parent.parent = Ingest_system/
INGEST_SYSTEM_DIR = Path(__file__).resolve().parent.parent

# Apuntar directamente a la carpeta data/
pdf_path = INGEST_SYSTEM_DIR / "data" / "001.pdf"

print(f"📍 Ruta absoluta calculada: {pdf_path}")
print(f"🔍 ¿Existe el archivo?: {pdf_path.exists()}")

if pdf_path.exists():
    pdf = pdfium.PdfDocument(pdf_path)
    print(f"📄 Número de páginas: {len(pdf)}")

    for i, page in enumerate(pdf):
        text_page = page.get_textpage()
        text = text_page.get_text_range().replace("\x00", "").strip()
        print(f"--- Página {i + 1} ---")
        print(f"Caracteres extraídos: {len(text)}")
        print("Muestra del texto:")
        print(text[:300])
else:
    print("❌ El archivo no se encontró. Archivos en data/:")
    data_dir = INGEST_SYSTEM_DIR / "data"
    if data_dir.exists():
        print(list(data_dir.glob("*")))