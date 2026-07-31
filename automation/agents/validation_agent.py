import os
import py_compile


class ValidationAgent:

    name = "validation_agent"


    def run(self, context):

        print("\nValidation Agent:")


        changes = context.get(
            "code_changes",
            {}
        )


        files = changes.get(
            "created_files",
            []
        )


        result = {
            "checked": [],
            "errors": [],
            "status": "approved"
        }


        for file in files:

            if os.path.exists(file):

                result["checked"].append(
                    file
                )

                try:

                    py_compile.compile(
                        file,
                        doraise=True
                    )


                except Exception as e:

                    result["errors"].append(
                        {
                            "file": file,
                            "error": str(e)
                        }
                    )


        if result["errors"]:

            result["status"] = "failed"


        context["validation"] = result


        print(
            "Checked:",
            len(result["checked"])
        )


        print(
            "Status:",
            result["status"]
        )


        return context
