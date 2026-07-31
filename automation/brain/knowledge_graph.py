import json
from pathlib import Path


class EngineeringKnowledgeGraph:

    def __init__(self):

        self.path = Path(
            "backend/app/brain/knowledge_graph.json"
        )

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


    def load(self):

        if not self.path.exists():

            return {
                "nodes": [],
                "relations": []
            }


        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



    def save(
        self,
        graph
    ):

        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                graph,
                f,
                indent=4,
                ensure_ascii=False
            )



    def add_relation(
        self,
        source,
        relation,
        target
    ):

        graph = self.load()


        graph["relations"].append(
            {
                "source": source,
                "relation": relation,
                "target": target
            }
        )


        self.save(
            graph
        )


        return graph



    def find_solution(
        self,
        problem
    ):

        graph = self.load()

        results = []


        for item in graph.get(
            "relations",
            []
        ):

            if item.get(
                "source"
            ) == problem:

                results.append(
                    item.get(
                        "target"
                    )
                )


        return results
