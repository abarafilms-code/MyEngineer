import os


class OpenAIClient:
    """OpenAI API connection layer."""

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def is_configured(self):
        return bool(self.api_key)

    def generate(self, prompt: str):
        return {
            "prompt": prompt,
            "status": "ready for OpenAI SDK integration"
        }
