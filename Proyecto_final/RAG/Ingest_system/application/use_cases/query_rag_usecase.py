from Ingest_system.application.ports.gemini_embedding_creator import GeminiEmbeddingCreator
from Ingest_system.application.ports.vector_store import VectorStore
from Ingest_system.application.ports.llm.llm_generator import LLMGenerator
from Ingest_system.domain.models.query import QueryResult


class QueryRAGUseCase:
    def __init__(
        self,
        embedding_service: GeminiEmbeddingCreator,
        vector_store: VectorStore,
        llm_service: LLMGenerator
    ):
        self.embedding_service = embedding_service
        self.vector_store = vector_store
        self.llm_service = llm_service

    def execute(self, question: str, top_k: int = 3) -> QueryResult:
        # 1. Convertir la pregunta en embedding
        query_embedding = self.embedding_service.create_embedding(question)

        # 2. Recuperar los chunks más afines desde ChromaDB
        relevant_chunks = self.vector_store.search_similar(query_embedding, top_k=top_k)

        # 3. Formatear el contexto recuperado
        context_text = "\n\n".join([c.text for c in relevant_chunks])

        # 4. Construir el prompt RAG con System Prompt estricto
        prompt = f"""Responde a la pregunta únicamente utilizando la información proporcionada en el siguiente contexto.
Si la respuesta no se encuentra en el contexto, indica explícitamente que no posees la información suficiente.

Contexto:
{context_text}

Pregunta: {question}
Respuesta:"""

        # 5. Generar la respuesta final
        answer = self.llm_service.generate_response(prompt)
        unique_sources = list(set([c.source for c in relevant_chunks]))

        return QueryResult(
            question=question,
            answer=answer,
            sources=unique_sources
        )