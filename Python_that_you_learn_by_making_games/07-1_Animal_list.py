# 동물 리스트를 만들기, 입력을 끝내려면 빈칸을 입력하기

import sys

# 동물 리스트 
animals = []
#사용자 입력 변수 초기화하기
userInput= " "

while userInput!="":
    userInput = sys.stdin.readline().strip()
    if len(userInput) >0 :
        animals.append(userInput)

animals.sort()
print(animals)