class ProductIntelligenceAgent:


    name = "product_intelligence_agent"



    def run(
        self,
        context
    ):

        cost = context.get(
            "cost",
            {}
        )


        production_cost = cost.get(
            "production_cost",
            0
        )


        price = cost.get(
            "recommended_price",
            0
        )


        profit = price - production_cost


        margin = 0

        if price:

            margin = (
                profit / price
            ) * 100



        context["product_analysis"] = {

            "production_cost": production_cost,

            "selling_price": price,

            "profit": round(
                profit,
                2
            ),

            "margin_percent": round(
                margin,
                2
            ),

            "decision":
                "PRODUCE"
                if margin > 40
                else
                "REVIEW"

        }


        print(
            "Product Intelligence:"
        )

        print(
            context["product_analysis"]
        )


        return context
