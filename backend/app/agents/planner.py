class PlannerAgent:

    name = "planner"

    def run(self, idea: str):
        return {
            "role": "product planner",
            "objective": "Define product requirements",
            "idea": idea,
            "questions": [
                "What problem does the product solve?",
                "Who is the target user?",
                "What are the constraints?"
            ]
        }
