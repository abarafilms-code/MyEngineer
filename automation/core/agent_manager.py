class AgentManager:


    name = "agent_manager"


    def __init__(self):

        self.pipeline = []


    def register(self, agent):

        self.pipeline.append(
            agent
        )


    def run(self, context):

        current_context = context


        for agent in self.pipeline:

            print(
                f"\nRunning {agent.name}..."
            )


            result = agent.run(
                current_context
            )


            if isinstance(result, dict):

                current_context = result


        return current_context
