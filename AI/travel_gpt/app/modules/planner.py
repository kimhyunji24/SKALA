from openai import OpenAI
import os
from dotenv import load_dotenv

# 환경 변수에서 API 키 불러오기
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def plan_trip(location: str, days: int) -> str:
    # 프롬프트 생성
    prompt = (
        f"Please create a detailed {days}-day travel itinerary for {location}. "
        f"Include major attractions, food recommendations, and daily highlights."
    )

    # GPT 호출
    res = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # 응답 반환
    return res.choices[0].message.content
