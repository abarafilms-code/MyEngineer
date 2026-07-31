import random


class RDAgent:

    name = "rd_agent"


    def run(self, context):

        ideas = [

            {
                "name": "industrial_mount",
                "category": "engineering",
                "complexity": "medium"
            },

            {
                "name": "robotic_adapter",
                "category": "automation",
                "complexity": "high"
            },

            {
                "name": "custom_tool_holder",
                "category": "manufacturing",
                "complexity": "low"
            },

            {
                "name": "repair_component",
                "category": "replacement_parts",
                "complexity": "medium"
            }

        ]


        selected = random.choice(
            ideas
        )


        research = {

            "generated_product":
                selected,

            "innovation_score":
                random.randint(70,95),

            "next_action":
                "CREATE_CAD_PROTOTYPE"

        }


        context["rd_research"] = research


        print(
            "R&D Agent:"
        )

        print(
            research
        )


        return context
