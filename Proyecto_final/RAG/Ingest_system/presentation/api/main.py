import os
from pathlib import Path
from dotenv import load_dotenv


# Encuentra la raíz del proyecto (3 niveles arriba desde presentation/api/main.py)
BASE_DIR = Path(__file__).resolve().parents[3]
env_path = BASE_DIR / ".env"

# Carga el .env forzando la ruta
load_dotenv(dotenv_path=env_path)

print(f"Ruta .env: {env_path}")
print(f"API Key cargada: {bool(os.getenv('GOOGLE_API_KEY'))}")

from Ingest_system.infrastructure.google.gemini_embedding_service import GeminiEmbeddingService

from fastapi import FastAPI, HTTPException
from fastapi.sse import EventSourceResponse
from pydantic import BaseModel
#Infrastructure
from Ingest_system.infrastructure.chunkers.recursive_chunker import RecursiveChunker
from Ingest_system.infrastructure.chromadb.chroma_vector_store import ChromaVectorStore
from Ingest_system.infrastructure.loaders.text_loader import TextLoader
from Ingest_system.infrastructure.google.gemini_llm_service import GeminiLLMService
#UseCases
from Ingest_system.application.use_cases.gemini_ingest_document_usecase import GeminiIngestDocumentsUseCase
from Ingest_system.application.use_cases.query_rag_usecase import QueryRAGUseCase
from Ingest_system.application.use_cases.query_rag_response_stream_usecase import QueryRAGResponseStreamUseCase
#modelMapping
from Ingest_system.presentation.schemas.query_schema import QueryResponseDTO, QueryRequestDTO


app = FastAPI(title="RAG API", version="1.0.0")

# Instanciación de componentes de Ingesta
chunker = RecursiveChunker(chunk_size=500, chunk_overlap=100)
embedding_service = GeminiEmbeddingService()
vector_store = ChromaVectorStore(persist_directory="chroma", collection_name="rag_collection")
loader = TextLoader()
llm_service = GeminiLLMService()

ingest_use_case = GeminiIngestDocumentsUseCase(
    chunker=chunker,
    embedding_service=embedding_service,
    vector_store=vector_store
)
query_rag_usecase = QueryRAGUseCase(
    embedding_service=embedding_service,
    vector_store=vector_store,
    llm_service=llm_service
)

query_rag_stream_usecase = QueryRAGResponseStreamUseCase(
    embedding_service=embedding_service,
    vector_store=vector_store,
    llm_service=llm_service
)

class IngestRequest(BaseModel):
    file_paths: list[str]


class QueryRequest(BaseModel):
    question: str
    top_k: int = 3

#---------------------------------------------------------------
#Endpoints
@app.get("/health")
def health_check():
    chroma_ok = vector_store.is_alive()
    if not chroma_ok:
        raise HTTPException(status_code=503, detail="ChromaDB no disponible")

    return {
        "status": "ok",
        "chroma": "connected",
        "total_indexed_chunks": vector_store.collection.count()
    }

@app.post("/ingest")
def ingest_documents(request: IngestRequest):
    try:
        documents = [loader.load(path) for path in request.file_paths]
        result = ingest_use_case.execute(documents)
        return {"message": "Ingesta completada exitosamente", **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query", response_model=QueryResponseDTO)
def query_rag(request: QueryRequestDTO):
    try:
        # Use Case returns a domain QueryResult object
        domain_result = query_rag_usecase.execute(
            question=request.question,
            top_k=request.top_k
        )

        # Converted to DTO for the API response
        return QueryResponseDTO(
            question=domain_result.question,
            answer=domain_result.answer,
            sources=domain_result.sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/chat/stream")
async def chat_stream(request: QueryRequestDTO):
    try:
        event_generator = query_rag_stream_usecase.execute(
            question=request.question,
            top_k=request.top_k
        )
        return EventSourceResponse(event_generator)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))