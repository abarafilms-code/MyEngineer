import json
import os
from datetime import datetime


class LearningLoopAgent:

    name = "learning_loop_agent"


    def run(self, context):

        decision = context.get(
            "ceo_decision",
            {}
        )

        quality = context.get(
            "quality_report",
            {}
        )

        market = context.get(
            "market_analysis",
            {}
        )


        lesson = {

            "timestamp":
                datetime.now().isoformat(),

            "decision":
                decision.get(
                    "final_decision",
                    "UNKNOWN"
                ),

            "quality_score":
                quality.get(
                    "quality_score",
                    0
                ),

            "market_score":
                market.get(
                    "market_score",
                    0
                ),

            "improvement":

                "Increase automation confidence"
                if quality.get("quality_score",0) > 90
                else
                "Improve validation rules"

        }


        os.makedirs(
            "automation/learning",
            exist_ok=True
        )


        with open(
            "automation/learning/lessons.json",
            "a"
        ) as f:

            f.write(
                json.dumps(lesson)
                + "\n"
            )


        context["learning"] = lesson


        print(
            "Learning Loop:"
        )

        print(
            lesson
        )


        return context
