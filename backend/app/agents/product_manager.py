class ProductManagerAgent:

    name = "product_manager"

    def run(self, idea: str):

        return {
            "category": "industrial product",
            "target_user": "engineering customer",
            "problem": f"Define market problem for: {idea}",
            "requirements": [
                "functional design",
                "user requirements",
                "production constraints"
            ],
            "constraints": [
                "cost optimization",
                "manufacturing feasibility",
                "serviceability"
            ]
        }
