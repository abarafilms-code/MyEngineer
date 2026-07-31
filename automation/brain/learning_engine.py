import json
from pathlib import Path
from datetime import datetime


class EngineeringLearningEngine:

    def __init__(self):

        self.path = Path(
            "backend/app/brain/engineering_rules.json"
        )

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


    def load(self):

        if not self.path.exists():

            return {
                "rules": []
            }


        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



    def learn_from_failure(
        self,
        failure
    ):

        data = self.load()


        rule = {

            "created":
                str(datetime.now()),

            "source":
                "failure_memory",

            "material":
                failure.get(
                    "material"
                ),

            "failure":
                failure.get(
                    "failure"
                ),

            "recommendation":
                self.generate_recommendation(
                    failure
                )
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



    def generate_recommendation(
        self,
        failure
    ):


        text = failure.get(
            "failure",
            ""
        ).lower()


        if "deformation" in text:

            return {
                "geometry":
                    "increase_wall_thickness",

                "value":
                    "+1mm"
            }


        if "thermal" in text:

            return {
                "material":
                    "upgrade_heat_resistance"
            }


        return {
            "action":
                "review_design"
        }
