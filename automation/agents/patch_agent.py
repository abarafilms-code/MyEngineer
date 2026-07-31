import os
import shutil
from datetime import datetime


class PatchAgent:

    name = "patch_agent"


    def run(self, context):

        print("\nPatch Agent:")


        files = context.get(
            "development",
            {}
        ).get(
            "analyzed_files",
            []
        )


        backup = []


        for file in files:

            if os.path.exists(file):

                backup_dir = "automation/memory/backups"

                os.makedirs(
                    backup_dir,
                    exist_ok=True
                )


                name = file.replace(
                    "/",
                    "_"
                )


                target = os.path.join(
                    backup_dir,
                    name + ".backup"
                )


                shutil.copy(
                    file,
                    target
                )


                backup.append(
                    target
                )


        context["patch"] = {

            "backup_files": backup,

            "status": "prepared",

            "timestamp": str(
                datetime.now()
            )

        }


        print(
            "Backups created:",
            len(backup)
        )


        return context
