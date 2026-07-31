from automation.core.context_agent import ContextAgent


class GeometryOptimizerAgent(ContextAgent):

    name = "geometry_optimizer_agent"


    def run(self, context):

        optimization = {

            "action": "optimize_geometry",

            "changes": {

                "wall_thickness_mm": "+1",

                "infill_percent": "+10",

                "support_strategy": "improved"

            },

            "status": "OPTIMIZED"

        }


        context["geometry_optimization"] = optimization


        engineering_context = context.get(
            "engineering_context"
        )


        if engineering_context:

            engineering_context.add_history(
                "Geometry optimization executed"
            )


        print(
            "Geometry Optimizer:",
            optimization
        )


        return context
