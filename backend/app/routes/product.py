from fastapi import APIRouter

router = APIRouter()

@router.post("/product/brief")
def create_product_brief(payload: dict):
    idea = payload.get("idea", "")

    return {
        "idea": idea,
        "category": "pending AI analysis",
        "materials": "pending AI analysis",
        "manufacturing": "pending AI analysis",
        "engineering_plan": "pending AI analysis"
    }
