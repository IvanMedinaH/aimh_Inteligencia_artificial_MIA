from Ingest_system.application.ports.chunker import Chunker
from Ingest_system.domain.models.chunk import Chunk


class RecursiveChunker(Chunker):
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str, source: str) -> list[Chunk]:
        chunks: list[Chunk] = []
        start = 0
        text_length = len(text)
        position = 0

        while start < text_length:
            end = start + self.chunk_size
            chunk_text = text[start:end]

            chunk_id = f"{source}_chunk_{position}"
            chunks.append(Chunk(
                id=chunk_id,
                text=chunk_text,
                source=source,
                position=position
            ))

            position += 1
            start += self.chunk_size - self.chunk_overlap

        return chunks