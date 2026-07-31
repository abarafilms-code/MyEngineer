class AgentManager:


    name = "agent_manager"


    def __init__(self):

        self.pipeline = []


    def register(self, agent):

        self.pipeline.append(agent)


    def run(self, context):

        results = {}

        for agent in self.pipeline:

            print(f"\nRunning {agent.name}...")

            result = agent.run(context)

            results[agent.name] = result

            context = result


        return results
