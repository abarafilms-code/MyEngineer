from automation.core.context_agent import ContextAgent

from automation.brain.experience_store import EngineeringExperienceStore
from automation.brain.rule_generator import EngineeringRuleGenerator
from automation.brain.rule_promotion import RulePromotionEngine


class SelfLearningAgent(ContextAgent):

    name="self_learning_agent"


    def __init__(self):

        self.memory = EngineeringExperienceStore()

        self.generator = EngineeringRuleGenerator()
        self.promoter = RulePromotionEngine()



    def run(
        self,
        context
    ):


        failures = context.get(
            "failures_detected",
            []
        )


        experience={

            "task":
            context.get("task"),

            "failures":
            failures,

            "material":
            context.get("material"),

            "result":
            "analyzed"

        }


        new_rules = self.generator.generate(
            failures
        )


        experience[
            "generated_rules"
        ] = new_rules


        self.memory.save(
            experience
        )


        context[
            "generated_rules"
        ] = new_rules


        promoted = self.promoter.promote()

        print(
            "Self Learning:",
            len(new_rules),
            "rules generated"
        )

        print(
            "Rule Promotion:",
            promoted,
            "rules activated"
        )


        return context
