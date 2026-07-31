from pydantic import BaseModel


class ProductBriefRequest(BaseModel):
    idea: str
