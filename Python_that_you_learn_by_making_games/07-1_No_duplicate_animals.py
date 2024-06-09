# 문제: 리스트에 있는 동물은 입력하지 못하도록 하기
import sys

animals = []
userInput = " "

while userInput!="":
    userInput=sys.stdin.readline().strip()
    if len(userInput)>0:
        if userInput not in animals:
            animals.append(userInput)
print(animals)