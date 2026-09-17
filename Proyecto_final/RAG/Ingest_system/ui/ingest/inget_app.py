import streamlit as st
import requests
from pathlib import Path
import os

API_URL = "http://localhost:8000"

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "Ingest_system" / "data"

st.set_page_config(page_title="RAG System", layout="wide")
st.title("📚 Sistema RAG - Módulo de Ingesta")

st.sidebar.header("Estado del Servidor")
try:
    response = requests.get(f"{API_URL}/health", timeout=2)
    if response.status_code == 200:
        st.sidebar.success("API activa 🟢")
    else:
        st.sidebar.error("API con problemas 🔴")
except Exception:
    st.sidebar.error("API desconectada 🔴")

st.header("1. Ingesta de Documentos")
st.write("Ingresa las rutas de los archivos localizados en la carpeta `data/` para indexarlos.")

data_folder = "data"
absolute_data_path = os.path.abspath(data_folder)
# Contenedor de verificación de ruta
with st.expander("🔍 Verificador de ruta de archivos", expanded=True):
    st.write(f"**Ruta buscada (relativa):** `{data_folder}`")
    st.write(f"**Ruta absoluta:** `{absolute_data_path}`")

    if os.path.exists(data_folder):
        st.success("✅ La carpeta de datos existe.")
        files = os.listdir(data_folder)
        st.write(f"**Archivos encontrados en carpeta:** {len(files)}")
    else:
        st.error("❌ La carpeta no existe en esa ubicación.")


available_files = []
if DATA_DIR.exists():
    # Obtener la ruta relativa desde la raíz del proyecto
    available_files = [
        str(f.relative_to(BASE_DIR)).replace("\\", "/")
        for f in DATA_DIR.glob("*")
        if f.suffix in ['.txt', '.md']
    ]

selected_files = st.multiselect(
    "Selecciona los documentos a ingerir:",
    options=available_files,
    default=available_files
)

if st.button("Iniciar Ingesta"):
    if not selected_files:
        st.warning("Selecciona al menos un archivo.")
    else:
        with st.spinner("Procesando documentos, generando embeddings y guardando en ChromaDB..."):
            try:
                res = requests.post(
                    f"{API_URL}/ingest",
                    json={"file_paths": selected_files}
                )
                if res.status_code == 200:
                    data = res.json()
                    st.success(f"✅ {data['message']}")
                    st.json(data)
                else:
                    st.error(f"Error en la ingesta: {res.text}")
            except Exception as e:
                st.error(f"No se pudo conectar con la API: {e}")