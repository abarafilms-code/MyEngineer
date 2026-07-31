class ToleranceAgent:

    name = "tolerance_agent"


    def run(self, context):

        tolerance = {

            "print_accuracy_mm": 0.2,

            "fit_quality": "GOOD",

            "recommendation": "READY_FOR_MANUFACTURING"

        }


        context["tolerance_analysis"] = tolerance


        print(
            "Tolerance Analysis:",
            tolerance
        )


        return context
