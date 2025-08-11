from fastapi import FastAPI, Query
from app.modules.stock import get_stock_price

app = FastAPI()

@app.get("/stock")
def stock(symbol: str = Query(...)):
    return {"price": get_stock_price(symbol)}