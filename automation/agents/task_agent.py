class TaskAgent:

    name = "task_agent"


    def run(self, context):

        task = context.lower()


        requirements = {
            "product": None,
            "materials": [],
            "features": [],
            "manufacturing": []
        }


        if "maestro" in task:
            requirements["product"] = "Maestro Solo component"


        if "корпус" in task or "enclosure" in task:
            requirements["features"].append(
                "protective enclosure"
            )


        materials = [
            "pla",
            "petg",
            "abs",
            "asa",
            "nylon",
            "peek"
        ]


        for material in materials:

            if material in task:

                requirements["materials"].append(
                    material.upper()
                )


        if "вентиля" in task or "ventilation" in task:

            requirements["features"].append(
                "ventilation system"
            )


        if "креп" in task or "mount" in task:

            requirements["features"].append(
                "mounting points"
            )


        return requirements
