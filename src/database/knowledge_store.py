"""
MyEngineer Knowledge Store

Initial memory layer for engineering knowledge.
"""


class KnowledgeStore:
    def __init__(self):
        self.storage = {
            "materials": [],
            "components": [],
            "projects": [],
            "solutions": []
        }

    def add(self, category: str, item):
        if category in self.storage:
            self.storage[category].append(item)

    def search(self, category: str):
        return self.storage.get(category, [])
