import sys

ascii_min = 32
ascii_max = 126

message = sys.stdin.readline()
key = list(map(int, str(314159)))

decrpt_mess = ""

for i in range(len(message)):
    temp = ord(message[i])
    if temp > ascii_max or temp< ascii_min :
        decrpt_mess += chr(temp)
    else:
        decrpt_mess += chr(temp - key[i % len(key)])
print(decrpt_mess)
