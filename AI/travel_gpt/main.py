from fastapi import FastAPI, Query
from app.modules.planner import plan_trip

app = FastAPI()

@app.get("/plan")
def plan(location: str = Query(...), days: int = Query(...)):
    return {"itinerary": plan_trip(location, days)}