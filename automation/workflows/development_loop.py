from automation.agents.planner_agent import PlannerAgent
from automation.agents.test_agent import TestAgent
from automation.agents.reviewer_agent import ReviewerAgent
from automation.agents.github_agent import GithubAgent


class DevelopmentLoop:

    def __init__(self):
        self.planner = PlannerAgent()
        self.test = TestAgent()
        self.review = ReviewerAgent()
        self.github = GithubAgent()


    def execute(self, task="Improve CAD generation system"):

        print("\nPlanning task:")
        print(task)

        plan = self.planner.run(task)

        print("\nDevelopment plan:")

        for step in plan["plan"]:
            print("-", step)


        print("\nRunning tests...")

        test_result = self.test.run()

        if not test_result["success"]:
            raise Exception(
                "Tests failed:\n" +
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
            "feat: execute planned development cycle"
        )

        self.github.push()

        print("Changes pushed")


if __name__ == "__main__":

    DevelopmentLoop().execute()
