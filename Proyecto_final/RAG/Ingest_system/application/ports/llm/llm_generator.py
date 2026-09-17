from abc import ABC, abstractmethod
from typing import Iterator


class LLMGenerator(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Genera una respuesta basada en el prompt del usuario y el contexto."""
        pass

    @abstractmethod
    def generate_response_stream(self, prompt: str) -> Iterator[str]:
        """Produce fragmentos de texto conforme el LLM los genera."""
        pass