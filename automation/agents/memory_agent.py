import json
import os
from datetime import datetime


class MemoryAgent:

    name = "memory_agent"


    memory_file = "automation/memory/history.json"


    def run(self, context):

        record = {
            "date": datetime.now().isoformat(),
            "task": context
        }


        os.makedirs(
            os.path.dirname(self.memory_file),
            exist_ok=True
        )


        history = []

        if os.path.exists(self.memory_file):

            with open(self.memory_file) as f:
                history = json.load(f)


        history.append(record)


        with open(self.memory_file,"w") as f:
            json.dump(
                history,
                f,
                indent=2
            )


        return {
            "saved": True
        }
