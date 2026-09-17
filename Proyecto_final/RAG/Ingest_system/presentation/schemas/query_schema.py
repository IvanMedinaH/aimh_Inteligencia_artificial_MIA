# Ingest_system/presentation/schemas/query_schema.py
from pydantic import BaseModel
from typing import List

class QueryRequestDTO(BaseModel):
    question: str
    top_k: int = 3

class QueryResponseDTO(BaseModel):
    question: str
    answer: str
    sources: List[str]