
class TaskPlanner:

    def plan(self, task):

        return {
            "objective": task,
            "steps":[
                "inspect",
                "modify",
                "validate",
                "publish"
            ]
        }
