from app.schemas.project import EngineeringProject

from app.agents.planner import PlannerAgent
from app.agents.researcher import ResearcherAgent
from app.agents.engineer import EngineerAgent
from app.agents.cad import CADAgent
from app.agents.manufacturing import ManufacturingAgent


class AgentPipeline:

    def __init__(self):

        self.planner = PlannerAgent()
        self.researcher = ResearcherAgent()
        self.engineer = EngineerAgent()
        self.cad = CADAgent()
        self.manufacturing = ManufacturingAgent()


    def run(self, idea: str):

        project = EngineeringProject(
            idea=idea
        )


        project.requirements = (
            self.planner.run(project)
        )


        research = (
            self.researcher.run(project)
        )

        project.materials = (
            research.get("materials", [])
        )


        engineering = (
            self.engineer.run(project)
        )

        project.requirements.extend(
            engineering.get("requirements", [])
        )


        cad = (
            self.cad.run(project)
        )

        project.cad_formats = (
            cad.get("formats", [])
        )


        manufacturing = (
            self.manufacturing.run(project)
        )

        project.manufacturing_methods = (
            manufacturing.get("process", [])
        )


        return project.model_dump()
