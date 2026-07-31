import json
import os
from datetime import datetime


class MemoryAgent:

    name = "memory_agent"


    def __init__(self):

        self.file = "automation/memory/history.json"


    def run(self, context):

        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )


        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "task": context.get("task"),
            "analysis": context.get("analysis"),
            "plan": context.get("plan"),
            "files_created": context.get("files"),
            "knowledge_loaded": list(
                context.get(
                    "knowledge",
                    {}
                ).keys()
            )
        }


        history = []


        if os.path.exists(self.file):

            with open(
                self.file,
                "r"
            ) as f:

                try:
                    history = json.load(f)

                except:
                    history = []


        history.append(
            record
        )


        with open(
            self.file,
            "w"
        ) as f:

            json.dump(
                history,
                f,
                indent=2
            )


        print(
            "Memory saved"
        )


        return {
            "memory_saved": True
        }
