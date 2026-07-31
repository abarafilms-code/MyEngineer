class ResearcherAgent:

    name = "researcher"

    def run(self, project):

        return {
            "materials": [
                "PETG",
                "ABS",
                "ASA",
                "PA-CF"
            ],
            "manufacturing_options": [
                "FDM 3D printing",
                "CNC machining",
                "Injection molding"
            ]
        }
