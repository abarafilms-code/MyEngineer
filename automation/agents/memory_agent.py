import json
import os
from datetime import datetime


class MemoryAgent:

    name = "memory_agent"

    memory_file = "automation/memory/history.json"


    def load(self):

        if not os.path.exists(self.memory_file):
            return []

        with open(self.memory_file, "r") as f:
            return json.load(f)


    def save(self, record):

        history = self.load()

        history.append(record)

        os.makedirs(
            os.path.dirname(self.memory_file),
            exist_ok=True
        )

        with open(self.memory_file, "w") as f:
            json.dump(
                history,
                f,
                indent=2
            )


    def run(self, task, result):

        record = {
            "date": datetime.now().isoformat(),
            "task": task,
            "result": result
        }

        self.save(record)

        return record
