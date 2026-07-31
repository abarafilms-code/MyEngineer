class WorkflowGraph:

    def __init__(self):

        self.graph = {}


    def add_node(self, name, next_nodes=None):

        self.graph[name] = next_nodes or []


    def get_next(self, name):

        return self.graph.get(
            name,
            []
        )


    def build_cad_workflow(self):

        self.add_node(
            "requirements_agent",
            [
                "architect_agent"
            ]
        )

        self.add_node(
            "architect_agent",
            [
                "cad_engineer_agent",
                "cost_engine_agent"
            ]
        )

        self.add_node(
            "cad_engineer_agent",
            [
                "cad_generator_agent"
            ]
        )

        self.add_node(
            "cad_generator_agent",
            [
                "stress_analysis_agent",
                "thermal_analysis_agent"
            ]
        )

        self.add_node(
            "stress_analysis_agent",
            [
                "manufacturing_agent"
            ]
        )

        self.add_node(
            "thermal_analysis_agent",
            [
                "manufacturing_agent"
            ]
        )

        self.add_node(
            "manufacturing_agent",
            []
        )


        return self.graph


    def resolve(self, start):

        visited = []

        queue = [
            start
        ]


        while queue:

            node = queue.pop(0)

            if node in visited:
                continue

            visited.append(node)

            queue.extend(
                self.get_next(node)
            )


        return visited
