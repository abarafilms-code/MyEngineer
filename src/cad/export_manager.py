"""CAD export pipeline prototype."""


class ExportManager:
    SUPPORTED_FORMATS = [
        "STEP",
        "STL",
        "DXF"
    ]

    def export(self, model, format_name):
        if format_name not in self.SUPPORTED_FORMATS:
            raise ValueError("Unsupported format")

        return {
            "model": model,
            "format": format_name,
            "status": "ready_for_export"
        }
