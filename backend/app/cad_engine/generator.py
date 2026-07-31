from backend.app.cad_engine.parameters import CADParameters


class CADGenerator:


    def __init__(self):

        self.parameters = CADParameters()



    def generate(self):

        return {
            "status": "generated",
            "parameters": self.parameters
        }
