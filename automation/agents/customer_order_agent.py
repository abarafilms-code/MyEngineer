class CustomerOrderAgent:

    name = "customer_order_agent"


    def run(self, context):

        order = {

            "customer": "AI_GENERATED_CUSTOMER",

            "product": "parametric_part",

            "quantity": 1,

            "requirements": {

                "material": "PETG",

                "manufacturing": "3D_PRINTING",

                "quality": "HIGH"

            },

            "status": "ORDER_RECEIVED"

        }


        context["customer_order"] = order


        print(
            "Customer Order:",
            order
        )


        return context
