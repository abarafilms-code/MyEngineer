class EnclosureGenerator:

    name = "enclosure_generator"

    def run(self, dimensions: dict):

        return {
            "type": "industrial_enclosure",
            "geometry": {
                "width": dimensions.get("width", "300mm"),
                "depth": dimensions.get("depth", "300mm"),
                "height": dimensions.get("height", "450mm")
            },
            "features": {
                "walls": {
                    "thickness": "3mm",
                    "reinforcement": True
                },
                "cover": {
                    "type": "removable",
                    "fastening": "screws"
                },
                "mounting": {
                    "points": 4
                }
            },
            "cad_ready": True
        }
