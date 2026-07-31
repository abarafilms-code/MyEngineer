class CostEngineAgent:


    name = "cost_engine_agent"


    def run(self, context):

        cad = context.get(
            "cad_kernel",
            {}
        )


        manufacturing = context.get(
            "manufacturing",
            {}
        )


        mass = cad.get(
            "estimated_mass_grams",
            0
        )


        material_cost = mass * 0.03


        electricity = 0.25 * 4


        production = (
            material_cost
            +
            electricity
        )


        price = production * 3


        context["cost"] = {

            "material_cost": round(
                material_cost,
                2
            ),

            "electricity_cost": round(
                electricity,
                2
            ),

            "production_cost": round(
                production,
                2
            ),

            "recommended_price": round(
                price,
                2
            )

        }


        print(
            "Cost Engine:"
        )

        print(
            context["cost"]
        )


        return context
