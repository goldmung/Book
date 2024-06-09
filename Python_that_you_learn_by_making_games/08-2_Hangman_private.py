# 1. 플레이어는 한 번에 한 문자만 입력, input은 입력에 제한X, 여러 문자를 입력할때 대처 방법 필요
# 2. 플레이어가 이겼는지 졌는지 판단 -> 리스트를 활용
# 3. 리스트는 원하는 순서대로 출력X, 입력 문자를 적절하게 출력하는 방법 필요
# 4. 마스킹한 단어(_ 나 *로 표현)를 출력, 어떤 문자를 맞췄고, 남은 문자가 몇자인지 플레이어에게 알림 

import sys

# 원하는 단어 임의로 입력
word = "apocalypse"
word= list(word)

# 추측한 값 확인하기 위한 변수
user_arr = ["_" for _ in range(len(word))]


while word != user_arr :
    # 사용자 입력 - 공백제거, 소문자 표현, 한글자만 입력되도록 설정
    userInput= sys.stdin.readline().strip().lower()
    if len(userInput) > 1:
        userInput = userInput[0]

    for i in range(len(word)):
        if word[i]== userInput :
            user_arr[i]= userInput
    count = 0
    for i in range(len(user_arr)):
        if user_arr[i]=="_": 
            count += 1

    print("맞춰야할 단어: ", "".join(word))
    print("현재까지의 결과: ", "".join(user_arr))
    print("남은 글자 개수: ", count)