import os
import json


class GeometryAgent:

    name = "geometry_agent"


    def run(self, context):

        print("\nGeometry Agent:")

        targets = [
            "backend/app/cad_engine"
        ]

        found = []

        for target in targets:

            if os.path.exists(target):

                for root, dirs, files in os.walk(target):

                    for file in files:

                        if file.endswith(".py"):

                            found.append(
                                os.path.join(root,file)
                            )


        report = {
            "modules": found,
            "count": len(found),
            "recommendations": [
                "add geometry validation",
                "add parametric constraints",
                "add solid verification",
                "add mesh quality checks"
            ]
        }


        print(
            "Geometry modules:",
            len(found)
        )


        context["geometry_report"] = report


        return context
