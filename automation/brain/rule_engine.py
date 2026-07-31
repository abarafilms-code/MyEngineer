import json
from pathlib import Path


class EngineeringRuleEngine:

    def __init__(self):

        self.path = Path(
            "backend/app/brain/engineering_rules.json"
        )

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


    def load_rules(self):

        if not self.path.exists():
            return []

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        return data.get(
            "rules",
            []
        )


    def apply_rules(
        self,
        context
    ):

        rules = self.load_rules()

        applied = []

        material = context.get(
            "material"
        )


        for rule in rules:

            if rule.get(
                "material"
            ) == material:

                applied.append(
                    rule
                )


        context[
            "engineering_rules"
        ] = applied


        return context


    def add_rule(
        self,
        rule
    ):

        data = {
            "rules": self.load_rules()
        }


        data["rules"].append(
            rule
        )


        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


        return rule
