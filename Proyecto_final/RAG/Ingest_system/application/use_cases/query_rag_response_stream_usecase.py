import json
from typing import AsyncIterator
from Ingest_system.application.ports.gemini_embedding_creator import GeminiEmbeddingCreator
from Ingest_system.application.ports.vector_store import VectorStore
from Ingest_system.application.ports.llm.llm_generator import LLMGenerator


class QueryRAGResponseStreamUseCase:
    def __init__(
            self,
            embedding_service: GeminiEmbeddingCreator,
            vector_store: VectorStore,
            llm_service: LLMGenerator
    ):
        self.embedding_service = embedding_service
        self.vector_store = vector_store
        self.llm_service = llm_service

    async def execute(self, question: str, top_k: int = 3) -> AsyncIterator[str]:
        # 1. Recuperación de contexto
        query_embedding = self.embedding_service.create_embedding(question)
        relevant_chunks = self.vector_store.search_similar(query_embedding, top_k=top_k)
        sources = list(set([c.source for c in relevant_chunks]))

        # 2. Emitir primero las fuentes en formato JSON
        sources_payload = json.dumps({"type": "sources", "sources": sources})
        yield f"data: {sources_payload}\n\n"

        # 3. Construir prompt RAG
        context_text = "\n\n".join([c.text for c in relevant_chunks])
        prompt = f"""Responde únicamente utilizando el siguiente contexto:

Contexto:
{context_text}

Pregunta: {question}
Respuesta:"""

        # 4. Transmitir el texto del LLM token a token
        for text_chunk in self.llm_service.generate_response_stream(prompt):
            token_payload = json.dumps({"type": "content", "delta": text_chunk})
            yield f"data: {token_payload}\n\n"