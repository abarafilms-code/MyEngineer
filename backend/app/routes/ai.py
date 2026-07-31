from fastapi import APIRouter
from fastapi import APIRouter
from fastapi import APIRouter

from app.ai.agent_runtime import AgentRuntime
from app.schemas.product import ProductBriefRequest


from fastapi import APIRouter

from app.ai.agent_runtime import AgentRuntime
from app.schemas.product import ProductBriefRequest


router = APIRouter()
runtime = AgentRuntime()


@router.post("/ai/product-brief")
def generate_product_brief(payload: ProductBriefRequest):

    return runtime.execute(payload.idea)
