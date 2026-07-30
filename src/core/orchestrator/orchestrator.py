"""
MyEngineer Core Orchestrator v0.1

Initial agent coordination layer.
"""


class EngineeringRequest:
    def __init__(self, description: str):
        self.description = description


class CoreOrchestrator:
    def __init__(self):
        self.agents = []

    def register_agent(self, agent):
        self.agents.append(agent)

    def process(self, request: EngineeringRequest):
        results = []
        for agent in self.agents:
            results.append(agent.run(request))

        return {
            "request": request.description,
            "results": results,
        }


if __name__ == "__main__":
    request = EngineeringRequest(
        "Create compact RO system for high rise cleaning"
    )

    orchestrator = CoreOrchestrator()
    print(orchestrator.process(request))
