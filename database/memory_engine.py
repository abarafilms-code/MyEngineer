class MemoryEngine:
    def __init__(self):
        self.records = []

    def store(self, item):
        self.records.append(item)

    def search(self, query):
        return [r for r in self.records if query.lower() in str(r).lower()]
