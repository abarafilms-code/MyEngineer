import subprocess


class TestAgent:

    name = "test_agent"

    def run(self):

        result = subprocess.run(
            ["pytest"],
            capture_output=True,
            text=True
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout + result.stderr
        }
