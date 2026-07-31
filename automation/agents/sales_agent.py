class SalesAgent:

    name = "sales_agent"


    def run(self, context):

        order = context.get(
            "customer_order",
            {}
        )


        sales = {

            "order_validated": True,

            "price_generated": True,

            "payment_status": "READY",

            "decision": "SEND_TO_ENGINEERING"

        }


        context["sales"] = sales


        print(
            "Sales Agent:",
            sales
        )


        return context
