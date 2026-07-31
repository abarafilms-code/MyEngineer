class PlannerAgent:

    name = "planner_agent"

    def run(self, task):

        steps = []

        task_lower = task.lower()

        if "cad" in task_lower or "geometry" in task_lower:
            steps.extend([
                "Analyze current CAD architecture",
                "Improve geometry generation modules",
                "Add validation for generated solids",
                "Run automated tests"
            ])

        else:
            steps.extend([
                "Analyze task requirements",
                "Identify required files",
                "Implement changes",
                "Run tests"
            ])

        return {
            "task": task,
            "plan": steps
        }
