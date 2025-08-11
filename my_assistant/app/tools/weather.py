import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(location: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric&lang=kr"
    res = requests.get(url)
    if res.status_code != 200:
        return f"날씨 정보를 불러올 수 없습니다: {res.text}"
    data = res.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    return f"{location}의 현재 날씨는 {desc}, 온도는 {temp}도입니다."