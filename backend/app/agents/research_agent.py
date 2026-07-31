from .base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    name = "research_agent"

    def run(self, task: str) -> dict:
        return {
            "agent": self.name,
            "research": "Find analogues, patents and market references",
            "task": task
        }
