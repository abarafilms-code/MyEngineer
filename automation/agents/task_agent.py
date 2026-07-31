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
            "keywords": []
        }


        keywords = []


        for word in [
            "cad",
            "geometry",
            "3d",
            "printing",
            "manufacturing",
            "engineering"
        ]:

            if word in task_lower:
                keywords.append(word)


        context["task_analysis"]["keywords"] = keywords


        print(
            "Task analyzed:",
            keywords
        )


        return context
