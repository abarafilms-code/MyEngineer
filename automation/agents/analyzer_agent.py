import os


class AnalyzerAgent:

    name = "analyzer_agent"


    def run(self, path="."):

        files = []

        for root, dirs, filenames in os.walk(path):

            # пропускаем служебные папки
            dirs[:] = [
                d for d in dirs
                if d not in [
                    ".git",
                    "__pycache__",
                    ".pytest_cache"
                ]
            ]

            for filename in filenames:

                if filename.endswith(".py"):

                    files.append(
                        os.path.join(root, filename)
                    )


        return {
            "files": files,
            "count": len(files)
        }
