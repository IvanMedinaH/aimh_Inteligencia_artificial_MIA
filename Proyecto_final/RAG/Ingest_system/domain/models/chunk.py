from dataclasses import dataclass


@dataclass
class Chunk:
    id: str
    text: str
    source: str
    position: int
    