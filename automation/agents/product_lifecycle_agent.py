class ProductLifecycleAgent:


    name = "product_lifecycle_agent"


    def run(
        self,
        context
    ):


        stages = [

            "IDEA",

            "DESIGN",

            "CAD",

            "SIMULATION",

            "PROTOTYPE",

            "PRODUCTION",

            "MARKET",

            "FEEDBACK"

        ]


        context["product_lifecycle"] = {

            "current_stage": "CAD",

            "stages": stages

        }


        print(
            "Lifecycle:",
            context["product_lifecycle"]
        )


        return context
