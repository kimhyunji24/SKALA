import re

def check_password_strength(password: str) -> list[str]:
    """
    비밀번호의 각 조건을 검사하여 충족되지 않은 조건 목록을 반환합니다.
    """
    errors = []
    
    # 조건 1: 영문 소문자 포함 여부
    if not re.search(r'[a-z]', password):
        errors.append("❌ 영문 소문자를 최소 1개 이상 포함해야 합니다.")
        
    # 조건 2: 영문 대문자 포함 여부
    if not re.search(r'[A-Z]', password):
        errors.append("❌ 영문 대문자를 최소 1개 이상 포함해야 합니다.")
        
    # 조건 3: 숫자 포함 여부
    if not re.search(r'\d', password):
        errors.append("❌ 숫자를 최소 1개 이상 포함해야 합니다.")
        
    # 조건 4: 특수문자 포함 여부
    if not re.search(r'[\W_]', password):
        errors.append("❌ 특수문자(!, @, # 등)를 최소 1개 이상 포함해야 합니다.")
        
    # 참고: 비밀번호 길이 조건도 추가하면 좋습니다.
    # if len(password) < 8:
    #     errors.append("❌ 비밀번호는 최소 8자 이상이어야 합니다.")
        
    return errors

# --- 메인 실행 부분 ---
if __name__ == "__main__":
    while True:
        user_password = input("검증할 비밀번호를 입력하세요: ")
        
        # 비밀번호의 미충족 조건 확인
        failed_conditions = check_password_strength(user_password)
        
        if not failed_conditions:
            print("\n✅ 모든 조건을 만족하는 안전한 비밀번호입니다!")
            break
        else:
            print("\n비밀번호가 아래의 조건을 만족하지 못했습니다:")
            # 충족되지 않은 모든 조건을 하나씩 출력
            for error in failed_conditions:
                print(error)
            print("\n다시 시도해주세요.")