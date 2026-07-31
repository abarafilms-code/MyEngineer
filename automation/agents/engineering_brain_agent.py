from automation.core.context_agent import ContextAgent

from automation.brain.rule_engine import EngineeringRuleEngine
from automation.brain.learning_engine import EngineeringLearningEngine
from automation.brain.decision_memory import EngineeringDecisionMemory
from automation.brain.knowledge_graph import EngineeringKnowledgeGraph


class EngineeringBrainAgent(ContextAgent):

    name = "engineering_brain_agent"


    def __init__(self):

        self.rules = EngineeringRuleEngine()
        self.learning = EngineeringLearningEngine()
        self.memory = EngineeringDecisionMemory()
        self.graph = EngineeringKnowledgeGraph()



    def run(
        self,
        context
    ):

        print(
            "\nEngineering Brain:"
        )


        context = self.rules.apply_rules(
            context
        )


        decision = self.memory.remember(
            context
        )


        context[
            "brain_memory"
        ] = decision



        material = context.get(
            "material"
        )


        if material:

            self.graph.add_relation(
                material,
                "validated_material",
                "engineering_database"
            )



        print(
            "Rules applied:",
            len(
                context.get(
                    "engineering_rules",
                    []
                )
            )
        )


        print(
            "Engineering memory saved"
        )


        return context
