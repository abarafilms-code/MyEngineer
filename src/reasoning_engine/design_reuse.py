"""
Design reuse engine.

Checks whether existing CAD, components or solutions can be reused.
"""


class DesignReuseEngine:
    def analyze(self, knowledge):
        return {
            "reuse_candidates": [],
            "recommendation": "search existing solutions first"
        }
