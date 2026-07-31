class ContextAgent:


    def update_context(self, context, section, value):

        engineering_context = context.get(
            "engineering_context"
        )

        if engineering_context:

            engineering_context.update(
                section,
                value
            )

        return context
