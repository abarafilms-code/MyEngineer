from dataclasses import dataclass, field


@dataclass
class EngineeringBrief:
    product: str
    materials: list = field(default_factory=list)
    manufacturing: list = field(default_factory=list)
    next_steps: list = field(default_factory=list)
