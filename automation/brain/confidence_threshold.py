class ConfidenceThreshold:

    MIN_CONFIDENCE = 0.8
    MIN_SUCCESS = 3

    @staticmethod
    def approve(rule):

        return (
            rule.get("confidence",0)
            >= ConfidenceThreshold.MIN_CONFIDENCE
            and
            rule.get("success",0)
            >= ConfidenceThreshold.MIN_SUCCESS
        )
