"""
Patent Collector prototype.

Future integrations:
- Google Patents
- Espacenet
- WIPO
- USPTO
"""


class PatentCollector:
    name = "patent_collector"

    def collect(self, query):
        return {
            "type": "patent",
            "query": query,
            "results": []
        }
