import json


class CADAgent:

    name = "cad_agent"


    def run(self, context):

        print("\nCAD analysis...")

        rules = []

        try:
            with open(
                "automation/knowledge/cad_rules.json"
            ) as f:
                data = json.load(f)

            rules = data["design_rules"]

        except Exception:
            pass


        context["cad_analysis"] = {
            "rules_checked": len(rules),
            "status": "ready",
            "recommendations": [
                r["description"]
                for r in rules
            ]
        }


        print(
            f"CAD rules loaded: {len(rules)}"
        )


        return context
