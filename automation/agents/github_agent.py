import subprocess


class GithubAgent:

    name = "github_agent"


    def commit(self, message):

        status = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True
        )

        if not status.stdout.strip():
            return {
                "committed": False,
                "message": "No changes"
            }


        subprocess.run(
            ["git", "add", "."],
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


        return {
            "committed": True,
            "message": message
        }


    def push(self):

        subprocess.run(
            [
                "git",
                "push"
            ],
            check=True
        )
