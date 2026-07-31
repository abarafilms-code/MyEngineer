class CEOAgent:

    name = "ceo_agent"


    def run(self, context):

        roi = context.get(
            "product_analysis",
            {}
        )

        market = context.get(
            "market_analysis",
            {}
        )

        quality = context.get(
            "quality_report",
            {}
        )


        profit = roi.get(
            "profit",
            0
        )

        market_score = market.get(
            "market_score",
            0
        )

        quality_score = quality.get(
            "quality_score",
            0
        )


        decision = "STOP"


        if (
            profit > 5
            and market_score > 70
            and quality_score > 90
        ):
            decision = "SCALE_PRODUCTION"


        elif (
            profit > 2
        ):
            decision = "TEST_MARKET"


        report = {

            "profit": profit,

            "market_score": market_score,

            "quality_score": quality_score,

            "final_decision": decision,

            "strategy":

                "Autonomous production approved"
                if decision == "SCALE_PRODUCTION"
                else
                "Needs optimization"

        }


        context["ceo_decision"] = report


        print(
            "CEO Agent:"
        )

        print(
            report
        )


        return context
