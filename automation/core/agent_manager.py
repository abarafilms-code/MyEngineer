class AgentManager:


    name = "agent_manager"


    def __init__(self):

        self.pipeline = []


    def register(self, agent):

        self.pipeline.append(agent)


    def run(self, task):

        context = {
            "task": task,
            "results": {}
        }


        for agent in self.pipeline:

            print(
                f"\nRunning {agent.name}..."
            )


            result = agent.run(
                context["task"]
            )


            context["results"][agent.name] = result


        return context
