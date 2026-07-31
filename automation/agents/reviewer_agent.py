

class ReviewerAgent:

    name = "reviewer_agent"

    def run(self, changes):

        issues = []

        if "TODO" in changes:
            issues.append(
                "Found unfinished TODO items"
            )

        return {
            "approved": len(issues) == 0,
            "issues": issues
        }
