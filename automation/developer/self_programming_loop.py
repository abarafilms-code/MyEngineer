from automation.developer.repository_analyzer import RepositoryAnalyzer
from automation.developer.code_planner import CodePlanner
from automation.developer.test_runner import TestRunner
from automation.developer.code_writer import CodeWriter


class SelfProgrammingLoop:


    def run(self, task):

        print(
            "=== MyEngineer Self Programming Loop ==="
        )


        analyzer = RepositoryAnalyzer()

        repo = analyzer.scan()


        planner = CodePlanner()

        plan = planner.create_plan(
            task,
            repo
        )


        print(
            "Plan:",
            plan
        )


        writer = CodeWriter()


        print(
            "Code Writer ready"
        )


        tester = TestRunner()

        result = tester.run()


        print(
            "Tests:",
            result
        )


        return {
            "repository": repo,
            "plan": plan,
            "tests": result
        }



if __name__ == "__main__":

    loop = SelfProgrammingLoop()

    loop.run(
        "Improve CAD generation system"
    )
