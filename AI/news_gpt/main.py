from fastapi import FastAPI, Query
from app.modules.search import search_news

app = FastAPI()

@app.get("/news")
def get_news(query: str = Query(...)):
    return {"results": search_news(query)}