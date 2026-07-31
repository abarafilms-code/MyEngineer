from automation.agents.analyzer_agent import AnalyzerAgent
from automation.agents.planner_agent import PlannerAgent
from automation.agents.coder_agent import CoderAgent
from automation.agents.test_agent import TestAgent
from automation.agents.reviewer_agent import ReviewerAgent
from automation.agents.github_agent import GithubAgent


class DevelopmentLoop:

    def __init__(self):
        self.analyzer = AnalyzerAgent()
        self.planner = PlannerAgent()
        self.coder = CoderAgent()
        self.test = TestAgent()
        self.review = ReviewerAgent()
        self.github = GithubAgent()


    def execute(self, task="Improve CAD generation system"):

        print("\nAnalyzing project...")

        analysis = self.analyzer.run()

        print(
            f"Found Python files: {analysis['count']}"
        )

        for file in analysis["files"][:10]:
            print("-", file)


        print("\nPlanning task:")

        plan = self.planner.run(task)

        for step in plan["plan"]:
            print("-", step)


        print("\nCoding...")

        code_result = self.coder.run(
            plan["plan"]
        )


        for file in code_result["files"]:
            print("Created:", file)


        print("\nRunning tests...")

        test_result = self.test.run()

        if not test_result["success"]:
            raise Exception(
                test_result["output"]
            )

        print("Tests passed")


        review = self.review.run(
            test_result["output"]
        )

        if not review["approved"]:
            raise Exception(
                review["issues"]
            )

        print("Review approved")


        self.github.commit(
            "feat: add analyzer agent cycle"
        )

        print("Changes committed")

        self.github.push()

        print("Changes pushed")


if __name__ == "__main__":
    DevelopmentLoop().execute()
