class DecisionAgent:

    name = "decision_agent"


    def run(self, context):

        task = context.get(
            "task",
            ""
        ).lower()


        decision = {
            "action": "general_improvement",
            "targets": [],
            "priority": "medium"
        }


        if "cad" in task or "geometry" in task:

            decision = {
                "action": "improve_cad_engine",
                "targets": [
                    "backend/app/cad_engine",
                    "backend/app/services",
                    "automation/agents"
                ],
                "priority": "high"
            }


        elif "test" in task:

            decision = {
                "action": "improve_testing",
                "targets": [
                    "tests",
                    "automation"
                ],
                "priority": "medium"
            }


        context["decision"] = decision


        print("\nDecision Agent:")
        print(
            decision
        )


        return context
