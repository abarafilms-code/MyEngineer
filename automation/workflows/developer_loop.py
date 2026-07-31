from automation.agents.developer_agent import DeveloperAgent
from automation.agents.git_agent import GitAgent
from automation.brain.task_planner import TaskPlanner


def run(task):

    print(
        "=== MyEngineer Developer Loop ==="
    )

    context = {
        "task": task
    }

    planner = TaskPlanner()

    context["plan"] = planner.plan(
        task
    )

    developer = DeveloperAgent()

    context = developer.run(
        context
    )

    git = GitAgent()

    git.run(
        "feat: autonomous developer agent update"
    )

    print(
        "Developer Loop Finished"
    )


if __name__ == "__main__":

    run(
        "Improve MyEngineer platform"
    )
