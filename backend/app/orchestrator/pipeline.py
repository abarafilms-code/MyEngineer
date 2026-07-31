from app.agents.product_manager import ProductManagerAgent
from app.agents.planner import PlannerAgent
from app.agents.researcher import ResearcherAgent
from app.agents.knowledge import KnowledgeAgent
from app.decision.engine import DecisionEngine
from app.agents.engineer import EngineerAgent
from app.agents.cad import CADAgent
from app.agents.manufacturing import ManufacturingAgent
from app.cost import CostEstimator

from app.cad_engine.intelligence.analyzer import CADAnalyzer
from app.cad_engine.intelligence.dimensions import DimensionEngine
from app.cad_engine.geometry.enclosure import EnclosureGenerator
from app.cad_engine.geometry.mounting import MountingGenerator


class AgentPipeline:

    def __init__(self):

        self.dimension_engine = DimensionEngine()
        self.enclosure_generator = EnclosureGenerator()
        self.mounting_generator = MountingGenerator()

        self.agents = [
            ProductManagerAgent(),
            PlannerAgent(),
            ResearcherAgent(),
            KnowledgeAgent(),
            DecisionEngine(),
            EngineerAgent(),
            CADAgent(),
            ManufacturingAgent(),
            CostEstimator(),
            CADAnalyzer()
        ]


    def run(self, idea: str):

        result = {
            "idea": idea
        }

        for agent in self.agents:
            result[agent.name] = agent.run(idea)

        dimensions = self.dimension_engine.run(idea)

        result["dimension_engine"] = dimensions

        result["enclosure_generator"] = self.enclosure_generator.run(
            dimensions["enclosure"]
        )

        result["mounting_generator"] = self.mounting_generator.run(idea)

        return result
