from automation.core.context_agent import ContextAgent


class DesignIterationAgent(ContextAgent):

    name = "design_iteration_agent"


    def run(self, context):

        decision = context.get(
            "design_decision",
            {}
        )


        if decision.get("status") == "REJECTED":

            context["iteration_required"] = True

        else:

            context["iteration_required"] = False


        print(
            "Design Iteration:",
            context["iteration_required"]
        )


        return context
