"""
Material selection logic.

Considers:
- environment;
- temperature;
- loads;
- manufacturing method.
"""


class MaterialSelector:
    def select(self, requirements):
        return {
            "material": "to be calculated",
            "criteria": requirements
        }
