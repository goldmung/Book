# 암호화키 = 314159로 했을 때 HELLO를 암호화하는 방법, 결과 KFPMT

word = "HELLO"
key = 314159
key_list = list(map(int, str(key)))
encrpt = ""

for i in range(len(word)):
   temp = ord(word[i])+key_list[i]
   encrpt += chr(temp)
print(encrpt)