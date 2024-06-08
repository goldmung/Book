import random

print("---영문---")
choices = "HT"
coinToss = random.choice(choices)
print(coinToss,"입니다.")

print("---한글---")
choices2 = ["앞면", "뒷면"]
coinToss2 = random.choices(choices2)
print(coinToss2, "입니다.")