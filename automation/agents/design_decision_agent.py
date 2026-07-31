from automation.core.context_agent import ContextAgent


class DesignDecisionAgent(ContextAgent):

    name = "design_decision_agent"


    def run(self, context):

        decision = {
            "status": "APPROVED",
            "action": "continue",
            "reason": "All validation checks passed"
        }


        if context.get("stress_analysis", {}).get("result") == "FAIL":

            decision = {
                "status": "REJECTED",
                "action": "optimize_geometry",
                "reason": "Stress failure"
            }


        context["design_decision"] = decision


        engineering_context = context.get(
            "engineering_context"
        )

        if engineering_context:

            engineering_context.add_decision(
                self.name,
                decision
            )


        print(
            "Design Decision:",
            decision
        )


        return context
