import os


class AIClient:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def generate(self, prompt: str):
        return {
            "prompt": prompt,
            "status": "AI client ready"
        }
