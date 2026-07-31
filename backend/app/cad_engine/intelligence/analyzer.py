class CADAnalyzer:

    name = "cad_analyzer"

    def run(self, idea: str):

        idea_lower = idea.lower()

        product_type = "industrial component"

        if "корпус" in idea_lower:
            product_type = "industrial enclosure"

        elif "крепление" in idea_lower:
            product_type = "mechanical mount"

        elif "деталь" in idea_lower:
            product_type = "replacement part"


        return {
            "product_type": product_type,
            "load_class": "medium",
            "environment": "industrial",
            "requirements": [
                "mechanical strength",
                "dimensional accuracy",
                "serviceability"
            ],
            "manufacturing": {
                "primary": "FDM 3D printing",
                "secondary": [
                    "CNC machining",
                    "injection molding"
                ]
            }
        }
