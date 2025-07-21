import requests
import sys

def get_github_user_info(username: str) -> dict | None:
    """
    GitHub API를 사용해 특정 사용자의 정보를 가져옵니다.

    Args:
        username (str): 정보를 조회할 GitHub 사용자 계정

    Returns:
        dict | None: 사용자 정보가 담긴 딕셔너리. 실패 시 None을 반환합니다.
    """
    api_url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            user_info = {
                "name": data.get("name"),
                "username": data.get("login"),
                "bio": data.get("bio"),
                "public_repos": data.get("public_repos"),
                "followers": data.get("followers"),
                "following": data.get("following"),
                "profile_url": data.get("html_url"),
                "created_at": data.get("created_at"),
            }
            return user_info
        elif response.status_code == 404:
            print(f"❌ 오류: 사용자 '{username}'를 찾을 수 없습니다.", file=sys.stderr)
            return None
        else:
            print(f"❌ 오류: API 요청 실패 (상태 코드: {response.status_code})", file=sys.stderr)
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ 오류: 네트워크 연결 문제 ({e})", file=sys.stderr)
        return None

# --- 메인 실행 부분 (사용자 입력 처리) ---
if __name__ == "__main__":
    while True:
        # 사용자로부터 계정 입력 받기
        username_input = input("조회할 GitHub 사용자 계정을 입력하세요 (종료하려면 'exit' 또는 '종료' 입력): ")
        
        # 종료 조건 확인
        if username_input.lower() in ['exit', '종료']:
            print("프로그램을 종료합니다.")
            break
        
        print(f"\n'{username_input}' 계정을 조회합니다...")
        
        # 함수를 호출하여 정보 가져오기
        user_data = get_github_user_info(username_input)
        
        # 결과 출력
        if user_data:
            print("✅ 정보 조회를 성공했습니다!")
            for key, value in user_data.items():
                print(f"- {key.replace('_', ' ').title()}: {value}")
        else:
            print("조회에 실패했습니다. 다른 계정으로 다시 시도해주세요.")
        
        print("\n" + "="*40)