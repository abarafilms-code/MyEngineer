"""CAD assembly management prototype."""


class AssemblyManager:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def get_structure(self):
        return {
            "parts_count": len(self.parts),
            "parts": self.parts
        }
