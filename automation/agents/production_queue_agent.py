class ProductionQueueAgent:


    name = "production_queue_agent"



    def run(
        self,
        context
    ):

        factory = context.get(
            "factory_plan",
            {}
        )


        queue = []


        if factory.get(
            "decision"
        ) == "START_PRODUCTION":

            queue.append({

                "product":
                    "parametric_part",

                "quantity":
                    factory.get(
                        "daily_capacity",
                        0
                    ),

                "status":
                    "QUEUED"

            })


        context["production_queue"] = queue


        print(
            "Production Queue:"
        )

        print(
            queue
        )


        return context
