class AgentController:
    def __init__(self):
        self.pipeline = [
            "planner",
            "researcher",
            "engineer",
            "cad"
        ]

    def run(self, idea: str):
        return {
            "idea": idea,
            "pipeline": self.pipeline,
            "status": "pipeline initialized"
        }
