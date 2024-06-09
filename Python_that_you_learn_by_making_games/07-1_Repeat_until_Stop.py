import sys

# 변수 선언
userInput = ""

# STOP을 입력할때까지 반복하기
while userInput !="STOP":
    userInput=sys.stdin.readline().upper().strip()
    print(userInput)