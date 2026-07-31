import subprocess
import sys
from datetime import datetime


class ReleaseManager:

    name = "release_manager"


    def run(self, task):

        print("=== MyEngineer Autonomous Release Manager ===")

        print("Task:", task)

        self.run_command(
            "python -m automation.developer.self_programming_loop"
        )

        self.run_command(
            "git status"
        )


        print(
            "Release prepared:",
            datetime.now()
        )


    def run_command(self, cmd):

        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )

        print(result.stdout)

        if result.stderr:
            print(result.stderr)


if __name__ == "__main__":

    task = " ".join(sys.argv[1:])

    ReleaseManager().run(task)
