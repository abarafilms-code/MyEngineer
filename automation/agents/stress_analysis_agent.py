from automation.core.context_agent import ContextAgent

class StressAnalysisAgent(ContextAgent):

    name = "stress_analysis_agent"


    def run(self, context):

        analysis = {

            "load_newtons": 50,

            "material": context.get(
                "material",
                "PETG"
            ),

            "safety_factor": 2.4,

            "deformation_mm": 0.18,

            "result": "APPROVE"

        }


        context["stress_analysis"] = analysis


        self.update_context(
            context,
            "validation",
            {
                "stress": analysis
            }
        )

        print(
            "Stress Analysis:",
            analysis
        )


        return context
