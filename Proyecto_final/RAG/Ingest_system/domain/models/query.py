# Ingest_system/domain/models/query.py
from dataclasses import dataclass
from typing import List

@dataclass
class QueryResult:
    question: str
    answer: str
    sources: List[str]