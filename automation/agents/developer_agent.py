from automation.core.context_agent import ContextAgent


class DeveloperAgent(ContextAgent):

    name = "developer_agent"

    def __init__(self):
        from automation.agents.code_writer_agent import CodeWriterAgent
        self.writer = CodeWriterAgent()

    def run(self, context):

        task = context.get(
            "task",
            ""
        )

        print(
            "Developer Agent:",
            task
        )

        plan = {
            "task": task,
            "actions": [
                "analyze_repository",
                "generate_patch",
                "run_tests"
            ]
        }

        context["development_plan"] = plan

        return self.writer.run(
            context
        )
