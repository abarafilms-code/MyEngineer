"""Research Agent prototype."""


class ResearchAgent:
    def analyze(self, topic: str):
        return {
            "topic": topic,
            "tasks": [
                "find analogues",
                "analyze technologies",
                "review patents"
            ]
        }
