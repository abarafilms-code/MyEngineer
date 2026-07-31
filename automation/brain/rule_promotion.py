import json
from pathlib import Path


class RulePromotionEngine:

    def __init__(self):

        self.experience_path = Path(
            "backend/app/brain/experience_memory.json"
        )

        self.rules_path = Path(
            "backend/app/brain/engineering_rules.json"
        )


    def promote(self):

        if not self.experience_path.exists():
            return 0


        with open(
            self.experience_path,
            "r",
            encoding="utf-8"
        ) as f:
            experiences = json.load(f)


        if not self.rules_path.exists():
            rules = {"rules": []}
        else:
            with open(
                self.rules_path,
                "r",
                encoding="utf-8"
            ) as f:
                rules = json.load(f)


        existing = {
            json.dumps(
                r,
                sort_keys=True
            )
            for r in rules.get("rules", [])
        }


        added = 0


        for exp in experiences:

            generated = exp.get(
                "generated_rules",
                []
            )


            for rule in generated:

                key = json.dumps(
                    rule,
                    sort_keys=True
                )


                if key not in existing:

                    rules["rules"].append(
                        rule
                    )

                    existing.add(
                        key
                    )

                    added += 1


        with open(
            self.rules_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                rules,
                f,
                indent=4,
                ensure_ascii=False
            )


        return added
