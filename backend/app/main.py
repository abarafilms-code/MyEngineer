from fastapi import FastAPI

app = FastAPI(title="MyEngineer API")

@app.get("/")
def health():
    return {"status": "MyEngineer online"}
