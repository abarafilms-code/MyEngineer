"""
Knowledge Graph prototype.

Stores engineering relationships between entities.
"""


class KnowledgeGraph:
    def __init__(self):
        self.nodes = []
        self.relationships = []

    def add_entity(self, entity_type, name, metadata=None):
        self.nodes.append({
            "type": entity_type,
            "name": name,
            "metadata": metadata or {}
        })

    def connect(self, source, relation, target):
        self.relationships.append({
            "source": source,
            "relation": relation,
            "target": target
        })

    def export(self):
        return {
            "nodes": self.nodes,
            "relationships": self.relationships
        }
