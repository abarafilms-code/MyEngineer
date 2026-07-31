from automation.brain.confidence_engine import ConfidenceEngine


class KnowledgeEvaluator:


    def __init__(self):

        self.engine = ConfidenceEngine()


    def evaluate_rule(
        self,
        rule_metrics
    ):

        return self.engine.evaluate(
            rule_metrics
        )
