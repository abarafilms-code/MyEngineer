from automation.core.agent_manager import AgentManager

from automation.agents.task_agent import TaskAgent
from automation.agents.analyzer_agent import AnalyzerAgent
from automation.agents.decision_agent import DecisionAgent
from automation.agents.planner_agent import PlannerAgent
from automation.agents.coder_agent import CoderAgent
from automation.agents.patch_agent import PatchAgent
from automation.agents.developer_agent import DeveloperAgent
from automation.agents.cad_engineer_agent import CADEngineerAgent
from automation.agents.geometry_agent import GeometryAgent
from automation.agents.cad_generator_agent import CADGeneratorAgent
from automation.agents.cad_kernel_agent import CADKernelAgent
from automation.agents.material_agent import MaterialAgent
from automation.agents.manufacturing_agent import ManufacturingAgent
from automation.agents.export_agent import ExportAgent
from automation.agents.simulation_agent import SimulationAgent
from automation.agents.test_agent import TestAgent
from automation.agents.reviewer_agent import ReviewerAgent
from automation.agents.knowledge_agent import KnowledgeAgent
from automation.agents.memory_agent import MemoryAgent



class AutonomousPipeline:


    def __init__(self):

        self.manager = AgentManager()


        self.manager.register(
            TaskAgent()
        )

        self.manager.register(
            AnalyzerAgent()
        )

        self.manager.register(
            DecisionAgent()
        )

        self.manager.register(
            PlannerAgent()
        )

        self.manager.register(
            DeveloperAgent()
        )

        self.manager.register(
            CADEngineerAgent()
        )

        self.manager.register(
            GeometryAgent()
        )

        self.manager.register(
            CADGeneratorAgent()
        )

        self.manager.register(
            CADKernelAgent()
        )

        self.manager.register(
            MaterialAgent()
        )

        self.manager.register(
            ManufacturingAgent()
        )

        self.manager.register(
            ExportAgent()
        )

        self.manager.register(
            SimulationAgent()
        )

        self.manager.register(
            CoderAgent()
        )

        self.manager.register(
            PatchAgent()
        )

        self.manager.register(
            TestAgent()
        )

        self.manager.register(
            ReviewerAgent()
        )

        self.manager.register(
            KnowledgeAgent()
        )

        self.manager.register(
            MemoryAgent()
        )



    def run(self, task):

        print(
            "\n=== MyEngineer Autonomous Pipeline ==="
        )


        context = {
            "task": task
        }


        result = self.manager.run(
            context
        )


        print(
            "\nPipeline finished"
        )


        return result
