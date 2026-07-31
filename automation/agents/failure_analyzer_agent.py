from automation.core.context_agent import ContextAgent


class FailureAnalyzerAgent(ContextAgent):

    name = "failure_analyzer_agent"

    def run(self, context):

        failures = []

        validation = context.get(
            "validation",
            {}
        )

        stress = validation.get(
            "stress",
            {}
        )

        thermal = validation.get(
            "thermal",
            {}
        )


        if stress.get("result") != "APPROVE":
            failures.append(
                "stress_failure"
            )


        if thermal.get("result") != "APPROVE":
            failures.append(
                "thermal_failure"
            )


        context[
            "failures_detected"
        ] = failures


        return context
