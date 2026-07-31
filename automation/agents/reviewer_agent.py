class ReviewerAgent:

    name = "reviewer_agent"


    def run(self, context):

        issues = []


        text = str(context)


        if "TODO" in text:
            issues.append(
                "Found unfinished TODO items"
            )


        return {
            "approved": len(issues) == 0,
            "issues": issues
        }
