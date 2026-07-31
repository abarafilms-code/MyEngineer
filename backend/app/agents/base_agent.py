"""Base class for MyEngineer AI agents."""


class BaseAgent:
    name = "base_agent"

    def run(self, task: str) -> dict:
        return {
            "agent": self.name,
            "task": task,
            "status": "initialized"
        }
