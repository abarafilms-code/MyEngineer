
from automation.agents.test_agent import TestAgent
from automation.agents.reviewer_agent import ReviewerAgent
from automation.agents.github_agent import GithubAgent


class DevelopmentLoop:


    def __init__(self):

        self.test = TestAgent()
        self.review = ReviewerAgent()
        self.github = GithubAgent()



    def execute(self):

        test_result = self.test.run()

        if not test_result["success"]:
            raise Exception(
                "Tests failed"
            )


        review = self.review.run(
            test_result["output"]
        )


        if not review["approved"]:
            raise Exception(
                review["issues"]
            )


        self.github.commit(
            "feat: autonomous development cycle"
        )

        self.github.push()


if __name__ == "__main__":

    DevelopmentLoop().execute()
