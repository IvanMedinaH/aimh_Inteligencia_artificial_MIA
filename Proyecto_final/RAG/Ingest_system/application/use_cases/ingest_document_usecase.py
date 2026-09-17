from Ingest_system.application.ports.chunker import Chunker
from Ingest_system.application.ports.google_embedding_creator import GoogleEmbeddingCreator
from Ingest_system.application.ports.vector_store import VectorStore
from Ingest_system.domain.models.document import Document


class IngestDocumentsUseCase:
    def __init__(
            self,
            chunker: Chunker,
            embedding_service: GoogleEmbeddingCreator,
            vector_store: VectorStore
    ):
        self.chunker = chunker
        self.embedding_service = embedding_service
        self.vector_store = vector_store

    def execute(self, documents: list[Document]) -> dict:
        total_chunks = 0
        for doc in documents:
            chunks = self.chunker.split(text=doc.content, source=doc.source)
            if not chunks:
                continue

            texts = [c.text for c in chunks]
            embeddings = self.embedding_service.embed_texts(texts)
            self.vector_store.save_chunks(chunks, embeddings)
            total_chunks += len(chunks)

        return {
            "processed_documents": len(documents),
            "indexed_chunks": total_chunks
        }