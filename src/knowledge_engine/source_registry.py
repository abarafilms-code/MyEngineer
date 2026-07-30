"""
Registry for engineering knowledge sources.
"""


class SourceRegistry:
    def __init__(self):
        self.sources = []

    def add(self, source_type, title, url=None):
        self.sources.append({
            "type": source_type,
            "title": title,
            "url": url
        })

    def all(self):
        return self.sources
