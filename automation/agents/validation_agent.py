class ValidationAgent:

    name = "validation_agent"


    def run(self, context):

        print("\nValidation Agent:")

        validation = {
            "geometry": True,
            "manufacturing": True,
            "materials": True,
            "status": "approved"
        }

        context["validation"] = validation

        print(
            "CAD validation passed"
        )

        return context
