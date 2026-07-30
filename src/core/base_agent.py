"""
Base Agent interface for MyEngineer.

All specialized engineering agents inherit this class.
"""


class BaseAgent:
    name = "base_agent"

    def run(self, context):
        raise NotImplementedError("Agent must implement run method")

    def describe(self):
        return {
            "agent": self.name,
            "status": "ready"
        }
