class TaskAgent:

    name = "task_agent"


    def run(self, context):

        task = context.get(
            "task",
            ""
        )


        task_lower = task.lower()


        context["task_analysis"] = {
            "original": task,
            "type": "engineering",
            "keywords": []
        }


        keywords = []


        if "cad" in task_lower:
            keywords.append("cad")

        if "geometry" in task_lower:
            keywords.append("geometry")

        if "print" in task_lower:
            keywords.append("3d_printing")


        context["task_analysis"]["keywords"] = keywords


        return context
