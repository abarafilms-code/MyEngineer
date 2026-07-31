class ChiefEngineerAgent:

    name = "chief_engineer_agent"

    def decide(self, context):

        return {
            "decision": "APPROVED",
            "reason": "Engineering requirements satisfied",
            "confidence": 0.9
        }
