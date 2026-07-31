class ManufacturingAgent:

    name = "manufacturing_agent"


    def run(self, context):

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


        print(
            "Manufacturing estimate created"
        )


        return context
