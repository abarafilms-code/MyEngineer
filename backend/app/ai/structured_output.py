from dataclasses import dataclass, field


@dataclass
class StructuredEngineeringOutput:
    product: str
    category: str = ""
    materials: list = field(default_factory=list)
    manufacturing: dict = field(default_factory=dict)
    cad_requirements: dict = field(default_factory=dict)
    next_steps: list = field(default_factory=list)
