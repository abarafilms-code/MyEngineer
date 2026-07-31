import json
from pathlib import Path
from datetime import datetime


class EngineeringExperienceStore:

    def __init__(self):

        self.path = Path(
            "backend/app/brain/experience_memory.json"
        )


        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


    def save(
        self,
        experience
    ):

        data = []

        if self.path.exists():

            with open(
                self.path,
                "r",
                encoding="utf-8"
            ) as f:
                data=json.load(f)


        experience[
            "timestamp"
        ] = str(datetime.now())


        data.append(
            experience
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


        return experience
