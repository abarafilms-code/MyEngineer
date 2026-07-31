class DimensionEngine:

    name = "dimension_engine"

    def run(self, idea: str):

        return {
            "enclosure": {
                "width": "300mm",
                "depth": "300mm",
                "height": "450mm"
            },
            "wall_thickness": "3mm",
            "mounting_points": 4,
            "ventilation": {
                "type": "passive",
                "vents": 12
            },
            "tolerance": "±0.2mm"
        }
