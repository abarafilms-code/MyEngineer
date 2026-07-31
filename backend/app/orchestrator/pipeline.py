from app.agents.planner import PlannerAgent
from app.agents.researcher import ResearcherAgent
from app.agents.engineer import EngineerAgent
from app.agents.cad import CADAgent
from app.agents.manufacturing import ManufacturingAgent


class AgentPipeline:

    def __init__(self):

        self.agents = [
            PlannerAgent(),
            ResearcherAgent(),
            EngineerAgent(),
            CADAgent(),
            ManufacturingAgent()
        ]


    def run(self, idea: str):

        result = {
            "product": idea,
            "status": "analysis complete"
        }


        for agent in self.agents:
            result[agent.name] = agent.run(idea)


        return result
