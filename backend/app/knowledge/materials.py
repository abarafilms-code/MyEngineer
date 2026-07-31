class MaterialKnowledge:

    def get_materials(self):

        return {
            "plastics": {
                "PLA": {
                    "use": "prototype",
                    "temperature": "low",
                    "strength": "medium"
                },

                "PETG": {
                    "use": "functional parts",
                    "temperature": "medium",
                    "strength": "good"
                },

                "ASA": {
                    "use": "industrial outdoor parts",
                    "temperature": "high",
                    "strength": "high",
                    "uv_resistance": True
                },

                "PA-CF": {
                    "use": "engineering components",
                    "temperature": "very high",
                    "strength": "very high"
                }
            }
        }
