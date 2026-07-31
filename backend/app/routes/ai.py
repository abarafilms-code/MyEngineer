from fastapi import APIRouter

from app.schemas.product import ProductBriefRequest
from app.orchestrator.pipeline import AgentPipeline


router = APIRouter()

pipeline = AgentPipeline()


@router.post("/ai/product-brief")
def generate_product_brief(
    payload: ProductBriefRequest
):

    return pipeline.run(payload.idea)
