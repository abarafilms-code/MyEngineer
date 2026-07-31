"""Product request data model foundation."""

from dataclasses import dataclass


@dataclass
class ProductRequest:
    idea: str
    target: str = "unknown"
    style: str = "not selected"
