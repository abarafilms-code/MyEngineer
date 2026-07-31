import os


class AnalyzerAgent:

    name = "analyzer_agent"


    def run(self, context):

        path = "."


        files = []


        for root, dirs, filenames in os.walk(path):

            dirs[:] = [
                d for d in dirs
                if d not in [
                    ".git",
                    "__pycache__",
                    ".pytest_cache",
                    ".venv"
                ]
            ]


            for filename in filenames:

                if filename.endswith(".py"):

                    files.append(
                        os.path.join(
                            root,
                            filename
                        )
                    )


        context["files"] = files


        context["analysis"] = {
            "python_files": len(files),
            "project_type": "python"
        }


        print(
            f"Analyzed files: {len(files)}"
        )


        return context
