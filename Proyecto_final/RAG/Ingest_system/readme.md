
# RAG System:

Hecho en python
Utilizando clean architecture para separacion de responsabilidades
y comunicacion limpia entre las capas.

El proyecto está construido sobre las siguientes tecnologías y herramientas clave:

---
>-   `google-genai`: SDK oficial de Google para interactuar con los modelos Gemini, encargado de la generación de respuestas y la creación de embeddings de texto.
>-   `chromadb`: Base de datos vectorial utilizada para almacenar, indexar y recuperar eficientemente los fragmentos de documentos (embeddings) relevantes para el contexto.
>-   `fastapi`: Framework web moderno y de alto rendimiento empleado para construir la API robusta que procesa las consultas del sistema RAG.
>-   `uvicorn`: Servidor web ASGI rápido y ligero que se encarga de ejecutar y desplegar la aplicación de FastAPI.
>-   `streamlit`: Herramienta utilizada para crear una interfaz de usuario web rápida e intuitiva, permitiendo interactuar con el sistema de manera visual.
>-   `pydantic`: Librería de validación de datos y gestión de configuraciones que garantiza el correcto modelado de las entradas y salidas de la API.
>-   `python-dotenv`: Módulo encargado de gestionar las variables de entorno (como las API keys) de forma segura desde un archivo `.env`.

---

Para correr la aplicacion 
FastAPI:
> posicionarse en la carpeta:
> >Ingest_system y arrancar con:<br>
> > **uvicorn Ingest_system.presentation.api.main:app --reload --port 8000**

Luego arrancar 
Streamlit:
CHAT: para realizar preguntas
>>streamlit run ui/chat_app.py

Ingest system : para agregar nuevos documentos que sirvan para consultar (txt, pdf, md)
>>streamlit run ui/ingest_app.py

<br> <br>
<br> <br>
<br> <br>

*Nota: si los comandos fallan es por que no se encuentra posicionado en la carpeta que debe 
desde la consola para ejecutarse, considerar eso.