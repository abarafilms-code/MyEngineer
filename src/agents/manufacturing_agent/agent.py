from src.core.base_agent import BaseAgent


class ManufacturingAgent(BaseAgent):
    name = "manufacturing_agent"

    def run(self, context):
        return {
            "agent": self.name,
            "manufacturing": {
                "print": ["Housing", "Brackets", "Covers"],
                "buy": ["Pump", "Membrane", "Electronics"]
            },
            "input": context
        }
