import json
import os


class ExportAgent:

    name = "export_agent"


    def run(self, context):

        os.makedirs(
            "backend/app/manufacturing/output",
            exist_ok=True
        )


        data = {

            "cad": context.get(
                "cad_kernel",
                {}
            ),

            "material": context.get(
                "material",
                {}
            ),

            "manufacturing": context.get(
                "manufacturing",
                {}

            )

        }


        with open(
            "backend/app/manufacturing/output/specification.json",
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )


        print(
            "Export created"
        )


        return context
