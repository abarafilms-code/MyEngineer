class CADAgent:

    name = "cad"

    def run(self, idea: str):

        return {
            "cad": {
                "model_type": "parametric CAD",
                "formats": [
                    "STEP",
                    "STL",
                    "OBJ"
                ],
                "software": [
                    "Fusion 360",
                    "FreeCAD",
                    "SolidWorks"
                ]
            }
        }
