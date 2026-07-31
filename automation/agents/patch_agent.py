class PatchAgent:

    name = "patch_agent"


    def run(self, context):

        print("\nPatch Agent:")

        patch = {
            "created": [],
            "modified": [],
            "status": "ready"
        }

        context["patch"] = patch

        print(
            "Patch prepared"
        )

        return context
