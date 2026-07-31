from dataclasses import dataclass, field


@dataclass
class CADRequirements:
    geometry: list = field(default_factory=list)
    formats: list = field(default_factory=list)
    constraints: list = field(default_factory=list)
