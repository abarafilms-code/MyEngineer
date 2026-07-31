class ChangeProposalAgent:

    def propose(self, task, repository):

        return {
            "task": task,
            "target": "backend/app",
            "change": "engineering improvement",
            "reason": "optimize reliability",
            "confidence": 0.85
        }
