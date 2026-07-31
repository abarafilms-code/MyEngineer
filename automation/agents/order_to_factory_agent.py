class OrderToFactoryAgent:

    name = "order_to_factory_agent"


    def run(self, context):

        production = {

            "order": "parametric_part",

            "queue_status": "ADDED",

            "priority": "NORMAL",

            "factory_command": "START_MANUFACTURING"

        }


        context["factory_order"] = production


        print(
            "Order To Factory:",
            production
        )


        return context
