import subprocess


class TestRunner:

    def run(self):

        result = subprocess.run(
            [
                "python",
                "-m",
                "py_compile",
                "automation/core/controller.py"
            ],
            capture_output=True,
            text=True
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout
        }
