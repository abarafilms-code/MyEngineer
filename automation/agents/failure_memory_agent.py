from automation.core.context_agent import ContextAgent


class FailureMemoryAgent(ContextAgent):

    name = "failure_memory_agent"


    def run(self, context):

        memory = {

            "previous_failures": [],

            "learned_rules": [

                "increase_wall_thickness",

                "improve_material_selection"

            ]

        }


        context["failure_memory"] = memory


        print(
            "Failure Memory:",
            memory
        )


        return context
