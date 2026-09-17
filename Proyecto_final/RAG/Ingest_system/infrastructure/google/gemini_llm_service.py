import os
import time
import logging
from typing import Iterator

from google import genai
from google.genai import types
from google.genai.errors import APIError
from Ingest_system.application.ports.llm.llm_generator import LLMGenerator

logger = logging.getLogger(__name__)

class GeminiLLMService(LLMGenerator):

    def __init__(
        self,
        api_key: str = None,
        models: list[str] = None
    ):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY no está configurada")

        self.client = genai.Client(api_key=self.api_key)
        # Modelos válidos y activos
        self.models = models or [
            "gemini-3.1-flash-lite"
            "gemini-3.5-flash-lite",  # Extremadamente rápido y de bajo costo para alta demanda
            "gemini-3.8-flash",       # El modelo insignia más rápido e inteligente para agentes (Sep 2026)
            "gemini-3.7-flash",       # Excelente balance y el anterior estándar para flujos complejos
            "gemini-3.6-flash",       # Tu modelo base actual
            "gemini-3.5-flash",       # Versión heredada muy veloz para tareas rutinarias
        ]

    def generate_response(self, prompt: str) -> str:
        last_error = None

        for model in self.models:
            # Reintentos por modelo en caso de 503 (High Demand)
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    response = self.client.models.generate_content(
                        model=model,
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
                        )
                    )
                    return response.text
                except APIError as e:
                    last_error = e
                    # Si es error 503 o 429, reintentamos con espera
                    if e.code in [503, 429]:
                        wait_time = (attempt + 1) * 2
                        logger.warning(
                            f"Modelo {model} ocupado ({e.code}). "
                            f"Reintentando intento {attempt + 1}/{max_retries} en {wait_time}s..."
                        )
                        time.sleep(wait_time)
                    else:
                        # Si es otro error (ej. 404), saltamos directo al siguiente modelo
                        break
                except Exception as e:
                    last_error = e
                    break

        raise RuntimeError(
            f"No se pudo completar la generación. Los modelos están temporalmente saturados. "
            f"Último error: {last_error}"
        )

    def generate_response_stream(self, prompt: str) -> Iterator[str]:
        """Transmite la respuesta token por token garantizando el tipado str."""
        last_error = None

        for model in self.models:
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    response_stream = self.client.models.generate_content_stream(
                        model=model,
                        contents=prompt,
                    )

                    for chunk in response_stream:
                        text_content = chunk.text
                        if text_content is not None and len(text_content) > 0:
                            yield text_content

                    # Si el stream se completó con éxito, finaliza la ejecución
                    return

                except APIError as e:
                    last_error = e
                    if e.code in [503, 429]:
                        wait_time = (attempt + 1) * 2
                        logger.warning(
                            f"Stream ocupado en modelo {model} ({e.code}). "
                            f"Reintentando {attempt + 1}/{max_retries} en {wait_time}s..."
                        )
                        time.sleep(wait_time)
                    else:
                        break
                except Exception as e:
                    last_error = e
                    break

        raise RuntimeError(
            f"No se pudo completar el streaming de respuesta. Último error: {last_error}"
        )
