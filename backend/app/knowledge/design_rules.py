class DesignRulesKnowledge:

    def get_rules(self):

        return {
            "fdm": {
                "wall_thickness": "2-4 mm",
                "tolerance": "±0.2 mm",
                "infill": "30-50%"
            },

            "industrial_parts": {
                "recommended_materials": [
                    "ASA",
                    "PETG",
                    "PA-CF"
                ]
            }
        }
