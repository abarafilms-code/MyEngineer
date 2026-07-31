class ManufacturingAgent:

    name = "manufacturing"

    def run(self, idea: str):

        return {
            "manufacturing": {
                "technology": "Additive manufacturing",
                "process": [
                    "prototype",
                    "testing",
                    "small batch production"
                ],
                "materials": [
                    "PETG",
                    "ABS",
                    "ASA"
                ]
            }
        }
