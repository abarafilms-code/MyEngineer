import json
from pathlib import Path


class RuleMetrics:

    def __init__(self):
        self.path = Path(
            "backend/app/brain/rule_metrics.json"
        )
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


    def load(self):

        if not self.path.exists():
            return {}

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)


    def update(
        self,
        rule,
        success=True
    ):

        data = self.load()

        if rule not in data:
            data[rule] = {
                "usage": 0,
                "success": 0,
                "failure": 0,
                "confidence": 0
            }


        data[rule]["usage"] += 1

        if success:
            data[rule]["success"] += 1
        else:
            data[rule]["failure"] += 1


        data[rule]["confidence"] = round(
            data[rule]["success"] /
            data[rule]["usage"],
            2
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

        return data[rule]
