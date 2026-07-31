from automation.core.context_agent import ContextAgent
from automation.core.cad_memory import CADMemory


class CADMemoryAgent(ContextAgent):

    name = "cad_memory_agent"


    def __init__(self):

        self.memory = CADMemory()


    def run(self, context):

        record = self.memory.remember(
            context
        )

        context["cad_memory"] = record

        print(
            "CAD Memory:",
            record
        )

        return context
