from dataclasses import dataclass, field


@dataclass
class ManufacturingPlan:
    technology: str
    equipment: list = field(default_factory=list)
    processes: list = field(default_factory=list)
    cost_estimate: str = "pending"
