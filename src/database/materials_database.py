"""Materials intelligence database prototype."""


class MaterialsDatabase:
    def __init__(self):
        self.materials = []

    def add_material(self, material):
        self.materials.append(material)

    def find_by_property(self, property_name, value):
        return [
            material for material in self.materials
            if material.get(property_name) == value
        ]
