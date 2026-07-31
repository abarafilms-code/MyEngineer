class ContextAdapter:

    def __init__(self, engineering_context):

        self.engineering_context = engineering_context


    def build_agent_context(self, task_context=None):

        context = {}

        if task_context:
            context.update(task_context)


        context["engineering_context"] = (
            self.engineering_context
        )


        return context


    def update_from_agent_result(self, agent_name, result):

        if not result:
            return


        ctx = self.engineering_context


        if hasattr(ctx, "add_history"):

            ctx.add_history(
                {
                    "agent": agent_name,
                    "result": result
                }
            )
