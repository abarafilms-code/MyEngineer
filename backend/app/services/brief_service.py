class BriefService:
    def build(self, idea: str):
        return {
            "idea": idea,
            "type": "engineering brief",
            "status": "generated"
        }
