# 특정 범위의 숫자를 맞히는 게임 (1,100)
# 사용자는 숫자가 큰지 작은지 힌트를 얻습니다.
# 게임이 끝나면 몇 번 시도했는지 알려줍니다.

import random
import sys

minNum = 1
maxNum = 100
userInput=""
count=0

randNum = random.randrange(minNum, maxNum+1)

while userInput!=randNum:
    userInput = sys.stdin.readline().rstrip()
    if not userInput.isnumeric():
        print(userInput,":이것은 숫자가 아닙니다.")
    else:
        count += 1
        userInput = int(userInput)
        if userInput < randNum:
            print("작습니다. 다시 입력하세요")
        elif userInput > randNum: 
            print("큽니다. 다시 입력하세요")
        else:
            print("정답입니다.")
            break;
print("시도 횟수: ", count)