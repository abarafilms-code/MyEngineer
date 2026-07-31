class CADParameters:

    def __init__(self):
        self.parameters = {
            "wall_thickness": "3mm",
            "tolerance": "±0.2mm",
            "infill": "40%",
            "material": "ASA",
            "printing_orientation": "optimized"
        }

    def get(self):
        return self.parameters
