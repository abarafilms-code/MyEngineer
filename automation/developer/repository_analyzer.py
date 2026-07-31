from pathlib import Path


class RepositoryAnalyzer:

    def scan(self):

        files = []

        for p in Path(".").rglob("*.py"):
            files.append(
                str(p)
            )

        return {
            "python_files": files,
            "count": len(files)
        }
