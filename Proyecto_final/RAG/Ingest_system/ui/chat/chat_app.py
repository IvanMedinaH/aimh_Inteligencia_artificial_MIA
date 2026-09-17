import streamlit as st
import requests

API_URL = "http://localhost:8000"



st.set_page_config(page_title="Asistente RAG", page_icon="💬", layout="centered")

st.title("💬 Asistente de Consulta RAG")
st.caption("Haz preguntas sobre la base de conocimiento cargada en el sistema.")

# Historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Panel lateral simplificado solo para el usuario
with st.sidebar:
    st.header("Opciones")
    top_k = st.slider("Precisión de respuesta (Documentos consultados)", min_value=1, max_value=8, value=3)
    if st.button("Limpiar conversación"):
        st.session_state.messages = []
        st.rerun()

# Renderizar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message and message["sources"]:
            with st.expander("Ver fuentes de información"):
                for src in message["sources"]:
                    st.caption(f"• `{src}`")

# Input del usuario
if prompt := st.chat_input("Escribe tu consulta aquí..."):
    # Dibujar pregunta del usuario
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Consultar al backend /query
    with st.chat_message("assistant"):
        with st.spinner("Procesando consulta..."):
            try:
                payload = {"question": prompt, "top_k": top_k}
                response = requests.post(f"{API_URL}/query", json=payload, timeout=60)

                if response.status_code == 200:
                    data = response.json()
                    answer = data.get("answer", "No se obtuvo respuesta.")
                    sources = data.get("sources", [])

                    st.markdown(answer)
                    if sources:
                        with st.expander("Ver fuentes de información"):
                            for src in sources:
                                st.caption(f"• `{src}`")

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    })
                else:
                    st.error(f"Error {response.status_code}: {response.text}")

            except requests.exceptions.RequestException as e:
                st.error(f"Error de conexión con el servidor: {e}")