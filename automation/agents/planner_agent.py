class PlannerAgent:

    name = "planner_agent"


    def run(self, context):

        task = context.get(
            "task",
            ""
        )


        task_lower = task.lower()


        steps = []


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


        context["plan"] = steps


        print("\nDevelopment plan:")

        for step in steps:
            print(
                "- " + step
            )


        return context
