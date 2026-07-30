"""
Vector Memory layer.

Future implementation:
- embeddings
- semantic search
- document similarity
- engineering knowledge retrieval
"""


class VectorMemory:
    def __init__(self):
        self.documents = []

    def add(self, document):
        self.documents.append(document)

    def search(self, query):
        return []
