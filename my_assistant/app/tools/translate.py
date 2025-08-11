import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate(text: str, target_lang: str = "ko") -> str:
    system_prompt = f"Translate the following text to {target_lang}"
    res = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )
    return res.choices[0].message.content