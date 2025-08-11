import requests
import os
from dotenv import load_dotenv

# load_dotenv()

# API_KEY = os.getenv("TAVILY_API_KEY")

# def search_news(query: str) -> list:
#     url = "https://api.tavily.com/search"
#     params = {"query": query, "api_key": API_KEY, "num_results": 3}
#     res = requests.get(url, params=params)
#     if res.status_code != 200:
#         return [f"뉴스 검색 실패: {res.text}"]
#     return [r['content'] for r in res.json().get("results", [])]
from tavily import TavilyClient

# .env 파일 로드
load_dotenv()

def search_news(query: str) -> list:
    """Tavily API를 사용해 뉴스를 검색하고 내용만 리스트로 반환합니다."""
    
    # .env 파일에서 API 키 가져오기
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return ["TAVILY_API_KEY가 .env 파일에 설정되지 않았습니다."]

    try:
        # Tavily 클라이언트 초기화
        client = TavilyClient(api_key=api_key)
        
        # 검색 실행 (결과 3개 요청)
        response = client.search(query=query, max_results=3)
        
        # 검색 결과에서 'content' 부분만 추출하여 리스트로 반환
        return [result['content'] for result in response.get("results", [])]
        
    except Exception as e:
        # API 키가 잘못되었거나 다른 에러가 발생한 경우
        return [f"뉴스 검색 중 에러 발생: {e}"]
