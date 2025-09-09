from langchain.llms.base import LLM
from typing import Optional, List
import requests

class LLaMAWrapper(LLM):
    endpoint: str  # ✅ must have a type annotation

    @property
    def _llm_type(self) -> str:
        return "llama"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = requests.post(
            self.endpoint,
            json={"model": "llama2", "prompt": prompt, "max_tokens": 512},

        )
        return response.json()['text']
