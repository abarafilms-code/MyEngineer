from automation.core.context_agent import ContextAgent


class CodeWriterAgent(ContextAgent):

    name = "code_writer_agent"

    def run(self, context):

        print(
            "Code Writer Agent: planning code changes"
        )

        context["code_changes"] = {
            "status": "READY",
            "files": []
        }

        return context
