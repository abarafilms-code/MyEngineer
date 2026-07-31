from automation.context.context_adapter import ContextAdapter


class AgentManager:

    def __init__(self):
        self.agents = []


    def register(self, agent):

        self.agents.append(agent)



    def run(self, context):

        result = context


        adapter = None

        if "engineering_context" in result:

            adapter = ContextAdapter(
                result["engineering_context"]
            )


        for agent in self.agents:

            print(
                f"Running {agent.name}..."
            )

            try:

                if adapter:

                    result = agent.run(
                        adapter.build_agent_context(result)
                    )

                else:

                    result = agent.run(
                        result
                    )

            except Exception as e:

                print(
                    f"{agent.name} failed:",
                    e
                )

                result["errors"] = result.get(
                    "errors",
                    []
                )

                result["errors"].append(
                    {
                        "agent": agent.name,
                        "error": str(e)
                    }
                )


        return result


    def run_route(self, context, route):

        result = context

        agent_map = {
            agent.name: agent
            for agent in self.agents
        }


        for agent_name in route:

            agent = agent_map.get(agent_name)

            if not agent:
                print(
                    f"Agent not found: {agent_name}"
                )
                continue


            print(
                f"Running routed {agent.name}..."
            )


            try:

                if "engineering_context" in result:

                    from automation.context.context_adapter import ContextAdapter

                    adapter = ContextAdapter(
                        result["engineering_context"]
                    )

                    result = agent.run(
                        adapter.build_agent_context(result)
                    )

                else:

                    result = agent.run(
                        result
                    )

            except Exception as e:

                print(
                    f"{agent.name} failed:",
                    e
                )

                result["errors"] = result.get(
                    "errors",
                    []
                )

                result["errors"].append(
                    {
                        "agent": agent.name,
                        "error": str(e)
                    }
                )


        return result

