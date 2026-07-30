from src.core.base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    name = "research_agent"

    def run(self, context):
        return {
            "agent": self.name,
            "research": [
                "Search analogues",
                "Analyze patents",
                "Collect technical references"
            ],
            "input": context
        }
