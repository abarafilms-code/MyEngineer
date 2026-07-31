class ResearcherAgent:

    name = "researcher"

    def run(self, idea: str):
        return {
            "research": f"Technology research for: {idea}",
            "materials": [
                "PLA",
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
