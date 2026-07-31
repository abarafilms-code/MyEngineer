class ConfidenceEngine:


    def evaluate(
        self,
        metrics
    ):

        confidence = metrics.get(
            "confidence",
            0
        )


        if confidence >= 0.85:
            status = "ACTIVE"

        elif confidence >= 0.5:
            status = "TESTING"

        else:
            status = "DEPRECATED"


        return {
            "confidence": confidence,
            "status": status
        }
