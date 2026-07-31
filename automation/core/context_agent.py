class ContextAgent:

    def update_context(self, context, section, values):

        engineering_context = context.get(
            "engineering_context"
        )

        if engineering_context:

            engineering_context.update(
                section,
                values
            )

        return context


    def add_decision(self, context, decision):

        engineering_context = context.get(
            "engineering_context"
        )

        if engineering_context:

            engineering_context.add_decision(
                self.name,
                decision
            )

        return context


    def add_history(self, context, event):

        engineering_context = context.get(
            "engineering_context"
        )

        if engineering_context:

            engineering_context.add_history(
                event
            )

        return context
