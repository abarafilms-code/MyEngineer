from src.core.base_agent import BaseAgent


class SupplyChainAgent(BaseAgent):
    name = "supply_chain_agent"

    def run(self, context):
        return {
            "agent": self.name,
            "bom": [
                "Pump",
                "RO membrane",
                "Filters",
                "Control electronics"
            ],
            "cost_analysis": "Initial estimation required",
            "input": context
        }
