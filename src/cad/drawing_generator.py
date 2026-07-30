"""Technical drawing generator prototype."""


class DrawingGenerator:
    def generate(self, model):
        return {
            "drawing": model,
            "formats": [
                "PDF",
                "DXF"
            ],
            "status": "drawing_definition_created"
        }
