class DecisionEngine:

    name = "decision_engine"

    def run(self, idea: str):

        idea_lower = idea.lower()

        if "корпус" in idea_lower or "корпус" in idea_lower:
            material = "ASA"
            reason = "Industrial enclosure requires UV resistance and durability"
        elif "нагруз" in idea_lower:
            material = "PA-CF"
            reason = "High mechanical strength requirement"
        else:
            material = "PETG"
            reason = "General engineering prototype"

        return {
            "recommended_material": material,
            "reason": reason,
            "parameters": {
                "wall_thickness": "3mm",
                "infill": "40%",
                "technology": "FDM",
                "nozzle_temperature": "250-260C",
                "bed_temperature": "80-100C"
            }
        }
