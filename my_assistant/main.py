from fastapi import FastAPI, Query
from app.tools.weather import get_weather
from app.tools.translate import translate

app = FastAPI()

@app.get("/weather")
def weather(location: str = Query(...)):
    return {"result": get_weather(location)}

@app.get("/translate")
def translate_api(text: str = Query(...), lang: str = Query("ko")):
    return {"result": translate(text, lang)}