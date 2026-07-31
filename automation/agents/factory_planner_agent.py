class FactoryPlannerAgent:


    name = "factory_planner_agent"



    def run(
        self,
        context
    ):

        product = context.get(
            "product_analysis",
            {}
        )


        decision = product.get(
            "decision",
            "REVIEW"
        )


        printers = 10

        print_hours = 4


        daily_capacity = printers * (
            24 / print_hours
        )


        profit = product.get(
            "profit",
            0
        )


        daily_profit = (
            daily_capacity *
            profit
        )


        context["factory_plan"] = {


            "printers": printers,

            "print_time_hours":
                print_hours,

            "daily_capacity":
                int(
                    daily_capacity
                ),

            "daily_profit":
                round(
                    daily_profit,
                    2
                ),

            "decision":
                "START_PRODUCTION"
                if decision == "PRODUCE"
                else
                "WAIT"

        }


        print(
            "Factory Planner:"
        )

        print(
            context["factory_plan"]
        )


        return context
