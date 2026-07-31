from automation.agents.test_agent import TestAgent
from automation.agents.reviewer_agent import ReviewerAgent
from automation.agents.github_agent import GithubAgent


class DevelopmentLoop:

    def __init__(self):
        self.test = TestAgent()
        self.review = ReviewerAgent()
        self.github = GithubAgent()


    def execute(self):

        print("Running tests...")

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


        commit_result = self.github.commit(
            "feat: autonomous development cycle"
        )


        if commit_result["committed"]:
            print("Changes committed")
            self.github.push()
            print("Changes pushed")
        else:
            print("No changes to commit")


if __name__ == "__main__":
    DevelopmentLoop().execute()
