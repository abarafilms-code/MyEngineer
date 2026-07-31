import json
import os


class KnowledgeAgent:

    name = "knowledge_agent"


    def __init__(self):

        self.database = "automation/knowledge/materials.json"


    def run(self, context):

        print("\nLoading engineering knowledge...")


        if not os.path.exists(self.database):

            return {
                "knowledge": {},
                "status": "database_missing"
            }


        with open(
            self.database,
            "r"
        ) as f:

            materials = json.load(f)


        context["knowledge"] = materials


        print(
            f"Loaded materials: {len(materials)}"
        )


        return context
