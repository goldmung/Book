#문제: 특정 범위의 숫자를 맞히는 게임
# 사용자는 숫자가 큰지 작은지 힌트를 얻음
# 게임이 끝나면 몇번 시도했는지 알 수 있음

import random
import sys

# 무작위 숫자 생성하기
randNum = random.randrange(1, 101)

# 사용자 입력
userNum = ""

# 사용자가 무작위 숫자를 맞출때까지 반복하기
while userNum!=randNum:
    userNum = sys.stdin.readline().strip()
    if not userNum.isnumeric():
        print(userNum, "이것은 숫자가 아닙니다.")
    else:
        userNum=int(userNum)
        if userNum < randNum:
            print("작습니다. 다시 입력하세요")
        elif userNum > randNum:
            print("큽니다. 다시 입력하세요")
        else:
            print("정답입니다.")