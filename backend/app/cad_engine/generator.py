from app.cad_engine.parameters import CADParameters
from app.cad_engine.constraints import CADConstraints
from app.cad_engine.templates import CADTemplates


class CADGenerator:

    name = "cad_generator"

    def __init__(self):
        self.parameters = CADParameters()
        self.constraints = CADConstraints()
        self.templates = CADTemplates()


    def run(self, idea: str):

        params = self.parameters.get()

        return {
            "idea": idea,
            "template": self.templates.industrial_enclosure(),
            "parameters": params,
            "constraints": self.constraints.check(params),
            "output_formats": [
                "STEP",
                "STL",
                "OBJ"
            ]
        }
