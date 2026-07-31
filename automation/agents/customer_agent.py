class CustomerAgent:

    name = "customer_agent"


    def run(self, context):

        market = context.get(
            "market_analysis",
            {}
        )


        customers = {

            "segments": market.get(
                "target_segments",
                []
            ),

            "buyer_profile": [

                "small manufacturers",

                "engineering companies",

                "designers",

                "repair services"

            ],

            "sales_priority": "B2B"

        }


        context["customers"] = customers


        print(
            "Customer Agent:"
        )

        print(
            customers
        )


        return context
