class ManufacturingWriter:

    def write(self, context, manufacturing):

        if "engineering_context" in context:

            context["engineering_context"].update(
                "manufacturing",
                manufacturing
            )

        return context
