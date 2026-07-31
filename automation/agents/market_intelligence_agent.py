class MarketIntelligenceAgent:

    name = "market_intelligence_agent"


    def run(self, context):

        product = context.get(
            "product",
            "parametric_part"
        )


        analysis = {

            "product": product,

            "market_demand": "HIGH",

            "target_segments": [
                "engineering",
                "automotive",
                "makers",
                "industrial repair"
            ],

            "competition_level": "MEDIUM",

            "recommended_channel": [
                "B2B",
                "online marketplace",
                "direct sales"
            ],

            "market_score": 87,

            "decision": "SCALE"

        }


        context["market_analysis"] = analysis


        print(
            "Market Intelligence:"
        )

        print(
            analysis
        )


        return context
