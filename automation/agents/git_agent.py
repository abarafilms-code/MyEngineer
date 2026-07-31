import subprocess


class GitAgent:

    def run(self, message):

        commands = [
            ["git","add","."],
            ["git","commit","-m",message],
            ["git","push"]
        ]

        for cmd in commands:
            subprocess.run(
                cmd,
                check=False
            )

        return {
            "git_status":"completed"
        }
