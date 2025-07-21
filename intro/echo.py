def echo_with_exit():
  """
  사용자로부터 문장을 계속 입력받아 출력합니다.
  '!quit'라고 입력하면 프로그램을 끝냅니다.
  """
  while True:
    sentence = input("문장을 입력하세요 (종료하려면 '!quit' 입력): ")
    if sentence == "!quit":
      print("프로그램을 종료합니다.")
      break  # 반복문을 탈출합니다.
    print(sentence)

# 함수 호출
echo_with_exit()