class ResponseParser:
    def parse(self, response: dict):
        return {
            "validated": True,
            "data": response
        }
