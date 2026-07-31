"""MyEngineer API entry point."""

from typing import Dict


def health_check() -> Dict[str, str]:
    return {"status": "ok", "service": "MyEngineer"}


if __name__ == "__main__":
    print(health_check())
