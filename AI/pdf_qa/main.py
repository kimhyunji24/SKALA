from fastapi import FastAPI, Query
from app.modules.qa import run_qa

app = FastAPI()

@app.get("/qa")
def qa(query: str = Query(...)):
    return {"result": run_qa(query)}