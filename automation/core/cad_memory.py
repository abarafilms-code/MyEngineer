import json
from pathlib import Path
from datetime import datetime


class CADMemory:

    def __init__(self):

        self.path = Path(
            "backend/app/reports/design_history.json"
        )

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


    def load(self):

        if not self.path.exists():
            return []

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def remember(
        self,
        context
    ):

        history = self.load()

        record = {

            "timestamp":
                str(datetime.now()),

            "task":
                context.get(
                    "task"
                ),

            "material":
                context.get(
                    "material"
                ),

            "geometry":
                context.get(
                    "geometry_report"
                ),

            "validation":
                {
                    "stress":
                        context.get(
                            "stress_analysis"
                        ),

                    "thermal":
                        context.get(
                            "thermal_analysis"
                        )
                },

            "decision":
                context.get(
                    "design_decision"
                ),

            "optimization":
                context.get(
                    "geometry_optimization"
                )

        }


        history.append(
            record
        )


        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                history,
                f,
                indent=4,
                ensure_ascii=False
            )


        return record
