from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class Document:
    id: str
    content: str
    source: str
    metadata: Dict[str, Any] = field(default_factory=dict)