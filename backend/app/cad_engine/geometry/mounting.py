class MountingGenerator:

    name = "mounting_generator"

    def run(self, idea: str):

        return {
            "mounting_system": {
                "screw_type": "M4",
                "mount_points": 4,
                "inserts": "heat_set_inserts",
                "boss_height": "12mm",
                "boss_diameter": "8mm"
            },
            "assembly": {
                "method": "screws",
                "serviceable": True,
                "tool": "hex_key"
            },
            "cad_ready": True
        }
