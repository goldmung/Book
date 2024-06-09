import sys

animals =[]
userInput = " "

while userInput!="":
    userInput = sys.stdin.readline().strip()
    if len(userInput) > 0:
        animals.append(userInput)

for i in animals:
    print(i)