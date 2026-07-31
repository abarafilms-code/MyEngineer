from automation.agents.test_agent import TestAgent
from automation.agents.reviewer_agent import ReviewerAgent


def test_test_agent_exists():
    agent = TestAgent()
    assert agent.name == "test_agent"


def test_reviewer_agent_approves_clean_code():
    agent = ReviewerAgent()

    result = agent.run(
        "clean implementation"
    )

    assert result["approved"] is True


def test_reviewer_agent_detects_todo():
    agent = ReviewerAgent()

    result = agent.run(
        "TODO: implement feature"
    )

    assert result["approved"] is False
