
import subprocess


class GithubAgent:

    name = "github_agent"


    def commit(self, message):

        subprocess.run(
            ["git","add","."],
            check=True
        )

        subprocess.run(
            [
                "git",
                "commit",
                "-m",
                message
            ],
            check=True
        )


    def push(self):

        subprocess.run(
            [
                "git",
                "push"
            ],
            check=True
        )
