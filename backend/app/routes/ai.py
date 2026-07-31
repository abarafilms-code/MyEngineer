from fastapi import APIRouter

from app.ai.agent_runtime import AgentRuntime

router = APIRouter()
runtime = AgentRuntime()


@router.post("/ai/product-brief")
def generate_product_brief(payload: dict):
    idea = payload.get("idea", "")

    return runtime.execute(idea)
