# 문자열이 키보다 긴 경우
# 암호화할 문자열 = "Hello World", key = 314159 , 키 반복 이용

import sys
# 사용할 범위 지정
ascii_min = 32
ascii_max = 126

#암호화 키
key = list(map(int, str(314159)))
# 암호화할 메시지 입력받기
arr = sys.stdin.readline()
#arr = "Hello Python"

encrpt_arr = ""
for i in range(len(arr)):
    temp = ord(arr[i])
    if temp > ascii_max or temp < ascii_min :
        encrpt_arr += chr(temp)
    else:
        encrpt_arr += chr(temp + int(key[i % len(key)])) 
print(encrpt_arr)