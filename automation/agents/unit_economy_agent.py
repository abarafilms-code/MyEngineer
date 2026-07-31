class UnitEconomyAgent:


    name = "unit_economy_agent"


    def run(
        self,
        context
    ):


        factory = {

            "units":100,

            "unit_price":20000,

            "capacity_share":0.01,

            "revenue_model":"production_profit_share"

        }


        context["unit_economy"] = factory


        print(
            "Unit Economy:",
            factory
        )


        return context
