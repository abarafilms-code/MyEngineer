from app.knowledge.materials import MaterialKnowledge
from app.knowledge.design_rules import DesignRulesKnowledge
from app.knowledge.manufacturing import ManufacturingKnowledge


class KnowledgeAgent:

    name = "knowledge"

    def __init__(self):

        self.materials = MaterialKnowledge()
        self.rules = DesignRulesKnowledge()
        self.manufacturing = ManufacturingKnowledge()


    def run(self, idea: str):

        return {
            "materials": self.materials.get_materials(),
            "design_rules": self.rules.get_rules(),
            "manufacturing": self.manufacturing.get_methods()
        }
