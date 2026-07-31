class AgentManager:


    name = "agent_manager"


    def __init__(self):

        self.pipeline = []


    def register(self, agent):

        self.pipeline.append(agent)


    def run(self, task):

        context = {
            "task": task,
            "files": [],
            "plan": [],
            "changes": [],
            "knowledge": {},
            "results": {}
        }


        for agent in self.pipeline:

            print(
                f"\nRunning {agent.name}..."
            )


            result = agent.run(
                context
            )


            if isinstance(result, dict):

                context.update(
                    result
                )


            context["results"][agent.name] = result


        return context
