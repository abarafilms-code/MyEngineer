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


    def apply_rules(self, context):

        rules = self.load_rules()

        applied = []


        validation = context.get(
            "validation",
            {}
        )


        stress = validation.get(
            "stress",
            {}
        )


        thermal = validation.get(
            "thermal",
            {}
        )


        safety_factor = stress.get(
            "safety_factor",
            0
        )


        deformation = stress.get(
            "deformation_mm",
            0
        )


        thermal_margin = thermal.get(
            "thermal_margin",
            0
        )


        for rule in rules:


            condition = rule.get(
                "condition"
            )


            if condition == "low_safety_factor":

                if safety_factor < 2:

                    applied.append(rule)



            elif condition == "high_deformation":

                if deformation > 0.5:

                    applied.append(rule)



            elif condition == "thermal_limit_close":

                if thermal_margin < 10:

                    applied.append(rule)



            elif condition == "print_failure":

                if context.get(
                    "manufacturing_failure"
                ):

                    applied.append(rule)



        context[
            "engineering_rules"
        ] = applied


        context[
            "engineering_actions"
        ] = [
            r.get("action")
            for r in applied
        ]


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
