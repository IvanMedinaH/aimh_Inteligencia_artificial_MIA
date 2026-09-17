from dataclasses import dataclass

@dataclass
class Citation:
    chunk_id: str
    source: str
    text: str
    score: float