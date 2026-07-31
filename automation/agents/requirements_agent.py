from automation.core.context_agent import ContextAgent


class RequirementsAgent(ContextAgent):

    name = "requirements_agent"


    def run(self, context):

        task = context.get(
            "task",
            ""
        )


        requirements = {

            "raw_request": task,

            "engineering_requirements": {

                "geometry": "parametric",

                "manufacturing": "3d_printing",

                "validation": True,

                "cost_analysis": True

            },

            "status": "READY_FOR_ENGINEERING"

        }


        context["requirements"] = requirements

        self.update_context(
            context,
            "requirements",
            requirements
        )


        print(
            "Requirements Agent:",
            requirements
        )


        return context
