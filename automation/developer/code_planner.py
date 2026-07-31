
class CodePlanner:

    def create_plan(self, task, repo):

        return {
            "task": task,
            "repository_size": repo["count"],
            "actions": [
                "inspect_code",
                "generate_change",
                "validate"
            ]
        }
