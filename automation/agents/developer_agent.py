import os


class DeveloperAgent:

    name = "developer_agent"


    def run(self, context):

        decision = context.get(
            "decision",
            {}
        )


        targets = decision.get(
            "targets",
            []
        )


        changed = []


        for target in targets:

            if os.path.exists(target):

                for root, dirs, files in os.walk(target):

                    for file in files:

                        if file.endswith(".py"):

                            path = os.path.join(
                                root,
                                file
                            )

                            changed.append(path)

                            if len(changed) >= 3:
                                break


                    if len(changed) >= 3:
                        break


        context["development"] = {

            "analyzed_files": changed,
            "status": "ready_for_modification"

        }


        print(
            "\nDeveloper Agent analyzed:"
        )


        for item in changed:

            print(
                "-",
                item
            )


        return context
