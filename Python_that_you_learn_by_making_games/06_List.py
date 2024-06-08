#리스트 만들기
animals = ["개", "개미", "고양이", "박쥐", "장어"]
list2 = ["염소", "이구아나", "하마"]

# 요소2 바꾸기
animals[2]="암소"

# 아이템 추가하기
animals.append("여우")

#리스트 합치기
animals.extend(list2)

# 리스트 요소 출력하기
# print(animals[2:4])

# 요소의 개수 묻기
# print(len(animals), "종류의 동물이 리스트에 있습니다.")

# 리스트 정렬하기
animals.sort()

# 리스트 출력하기
print(animals)

# 리스트에 염소가 있는지?
if "염소" in animals:
    print("예, 리스트에 염소가 있습니다.", animals.index("염소"))
else:
    print("아니오, 리스트에 염소는 없습니다.")