import os


class OpenAIService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def generate_brief(self, idea: str):
        return {
            "idea": idea,
            "status": "OpenAI integration ready"
        }
