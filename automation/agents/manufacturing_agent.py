from automation.core.context_agent import ContextAgent
from automation.core.manufacturing_writer import ManufacturingWriter

class ManufacturingAgent(ContextAgent):

    name = "manufacturing_agent"


    def run(self, context):

        writer = ManufacturingWriter()

        material = context.get(
            "material",
            {}
        )


        context["manufacturing"] = {

            "print_time_hours": 4,

            "mass_grams": 120,

            "material": material.get(
                "name",
                "unknown"
            ),

            "estimated_cost": 8.5

        }


        self.update_context(
            context,
            "manufacturing",
            {
                "process": "3d_printing",
                "printer": "MyEngineer Farm",
                "print_time_hours": 4,
                "cost": 8.5
            }
        )

        print(
            "Manufacturing estimate created"
        )


        writer.write(
            context,
            context["manufacturing"]
        )

        return context
