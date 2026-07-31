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
from automation.agents.requirements_agent import RequirementsAgent
from automation.agents.design_review_agent import DesignReviewAgent
from automation.agents.failure_prediction_agent import FailurePredictionAgent

from automation.agents.architect_agent import ArchitectAgent
from automation.agents.material_agent import MaterialAgent
from automation.agents.manufacturing_agent import ManufacturingAgent
from automation.agents.export_agent import ExportAgent
from automation.agents.cost_engine_agent import CostEngineAgent
from automation.agents.product_intelligence_agent import ProductIntelligenceAgent
from automation.agents.factory_planner_agent import FactoryPlannerAgent
from automation.agents.production_queue_agent import ProductionQueueAgent
from automation.agents.printer_farm_agent import PrinterFarmAgent
from automation.agents.quality_control_agent import QualityControlAgent
from automation.agents.market_intelligence_agent import MarketIntelligenceAgent
from automation.agents.customer_agent import CustomerAgent
from automation.agents.ceo_agent import CEOAgent
from automation.agents.learning_loop_agent import LearningLoopAgent
from automation.agents.rd_agent import RDAgent
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
            CostEngineAgent()
        )

        self.manager.register(
            ProductIntelligenceAgent()
        )

        self.manager.register(
            FactoryPlannerAgent()
        )

        self.manager.register(
            ProductionQueueAgent()
        )

        self.manager.register(
            PrinterFarmAgent()
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
