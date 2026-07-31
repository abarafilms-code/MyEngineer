class MaterialAgent:

    name = "material_agent"


    def run(self, context):

        task = context.get(
            "task",
            ""
        ).lower()


        material = "PETG"


        if "outdoor" in task:
            material = "ASA"

        if "strong" in task or "mechanical" in task:
            material = "PA6_CF"


        context["material"] = {

            "name": material,

            "reason": "selected by engineering rules"

        }


        print(
            "Material selected:",
            material
        )


        return context
