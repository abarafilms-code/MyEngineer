"""MyEngineer API prototype."""


def health_check():
    return {
        "status": "running",
        "service": "MyEngineer Core"
    }


if __name__ == "__main__":
    print(health_check())
