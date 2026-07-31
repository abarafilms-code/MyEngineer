from app.agents.product_manager import ProductManagerAgent
from app.agents.planner import PlannerAgent
from app.agents.researcher import ResearcherAgent
from app.agents.knowledge import KnowledgeAgent
from app.decision.engine import DecisionEngine
from app.agents.engineer import EngineerAgent
from app.agents.cad import CADAgent
from app.agents.manufacturing import ManufacturingAgent
from app.agents.design_review import DesignReviewAgent
from app.cost import CostEstimator


class AgentPipeline:

    def __init__(self):

        self.agents = [
            ProductManagerAgent(),
            PlannerAgent(),
            ResearcherAgent(),
            KnowledgeAgent(),
            DecisionEngine(),
            EngineerAgent(),
            CADAgent(),
            ManufacturingAgent(),
            DesignReviewAgent(),
            CostEstimator()
        ]

    def run(self, idea: str):

        result = {
            "idea": idea
        }

        for agent in self.agents:
            result[agent.name] = agent.run(idea)

        return result
