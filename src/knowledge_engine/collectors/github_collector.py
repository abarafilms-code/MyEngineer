"""
GitHub Collector prototype.

Collects engineering repositories,
open hardware projects and CAD resources.
"""


class GitHubCollector:
    name = "github_collector"

    def collect(self, query):
        return {
            "type": "repository",
            "query": query,
            "results": []
        }
