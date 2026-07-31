from fastapi import FastAPI

from app.routes.ai import router as ai_router

app = FastAPI(title="MyEngineer API")

app.include_router(ai_router)


@app.get("/")
def health():
    return {"status": "MyEngineer MVP online"}
