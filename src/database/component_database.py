"""Component intelligence database prototype."""


class ComponentDatabase:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def find_alternatives(self, component_type):
        return [
            item for item in self.components
            if item.get("type") == component_type
        ]
