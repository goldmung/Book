import datetime

year = int(input("태어난 해는 언제인가요?"))
month = int(input("태어난 달는 언제인가요?"))
day = int(input("태어난 날는 언제인가요?"))

bday = datetime.datetime(year, month, day)

#요일 계산하기
if bday.weekday()==6:
    dow = "일"
elif bday.weekday()==0:
    dow = "월"
elif bday.weekday()==1:
    dow = "화"
elif bday.weekday()==2:
    dow = "수"
elif bday.weekday()==3:
    dow = "목"
elif bday.weekday()==4:
    dow = "금"
elif bday.weekday()==5:
    dow = "토"

# 결과 출력하기
print("태어난 요일은",dow, "입니다.")