from pydantic import BaseModel
from typing import List, Dict


class EngineeringProject(BaseModel):

    idea: str

    requirements: List[str] = []

    materials: List[str] = []

    cad_formats: List[str] = []

    manufacturing_methods: List[str] = []

    risks: List[str] = []

    estimates: Dict = {}
