import chromadb
from Ingest_system.application.ports.vector_store import VectorStore
from Ingest_system.domain.models.chunk import Chunk

class ChromaVectorStore(VectorStore):
    def __init__(self, persist_directory: str = "chroma", collection_name: str = "rag_collection"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def is_alive(self) -> bool:
        """Verifica que el cliente y la colección responden correctamente."""
        try:
            # heartbeat verifica la salud del motor de Chroma
            self.client.heartbeat()
            # realiza una lectura ligera sobre la colección
            self.collection.count()
            return True
        except Exception:
            return False

    def save_chunks(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        if not chunks:
            return

        ids = [c.id for c in chunks]
        documents = [c.text for c in chunks]
        metadatas = [{"source": c.source, "position": c.position} for c in chunks]

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search_similar(self, query_embedding: list[float], top_k: int = 3) -> list[Chunk]:
        """Busca y mapea los resultados de ChromaDB a objetos Chunk de dominio."""
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=["documents", "metadatas"]
        )

        retrieved_chunks: list[Chunk] = []

        if results["documents"] and results["documents"][0]:
            docs = results["documents"][0]
            metas = results["metadatas"][0] if results["metadatas"] else [{}] * len(docs)
            ids = results["ids"][0] if results["ids"] else [f"chunk_{i}" for i in range(len(docs))]

            for chunk_id, doc_text, meta in zip(ids, docs, metas):
                # Conversión explícita a tipos primitivos esperados por la dataclass Chunk
                raw_source = meta.get("source") if meta else None
                raw_position = meta.get("position") if meta else None

                source_val = str(raw_source) if raw_source is not None else "Desconocido"

                try:
                    # Convertimos primero a str para garantizar un tipo aceptado por int()
                    position_val = int(str(raw_position)) if raw_position is not None else 0
                except (ValueError, TypeError):
                    position_val = 0

                chunk = Chunk(
                    id=str(chunk_id),
                    text=str(doc_text),
                    source=source_val,
                    position=position_val
                )
                retrieved_chunks.append(chunk)

        return retrieved_chunks