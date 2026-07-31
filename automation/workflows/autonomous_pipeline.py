from automation.core.agent_manager import AgentManager

from automation.agents.task_agent import TaskAgent
from automation.agents.analyzer_agent import AnalyzerAgent
from automation.agents.planner_agent import PlannerAgent
from automation.agents.coder_agent import CoderAgent
from automation.agents.test_agent import TestAgent
from automation.agents.reviewer_agent import ReviewerAgent
from automation.agents.memory_agent import MemoryAgent
from automation.agents.knowledge_agent import KnowledgeAgent


class AutonomousPipeline:


    def __init__(self):

        self.manager = AgentManager()

        self.manager.register(
            TaskAgent()
        )

        self.manager.register(
            AnalyzerAgent()
        )

        self.manager.register(
            PlannerAgent()
        )

        self.manager.register(
            CoderAgent()
        )

        self.manager.register(
            TestAgent()
        )

        self.manager.register(
            ReviewerAgent()
        )

        self.manager.register(
            KnowledgeAgent()
        )

        self.manager.register(
            MemoryAgent()
        )


    def run(self, task):

        print("\n=== MyEngineer Autonomous Pipeline ===")

        result = self.manager.run(
            task
        )

        print("\nPipeline finished")

        return result
