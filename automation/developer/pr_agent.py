class PRAgent:

    def create(self, patch):

        return {
            "pull_request":
            "created",

            "status":
            "READY_FOR_REVIEW",

            "patch":
            patch
        }
