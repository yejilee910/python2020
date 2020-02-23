
# 현재 월을 변수에 저장합니다.

import datetime
x = datetime.datetime.now()
print(x)
month=x.month




# 조건문으로 계절을 확인합니다.

if month >= 2 and month <=11 :
    print("winter")
elif month >=3 and month >=5 :
    print("spring")
elif month >=6 and month >= 8 :
    print("summer")
else :
    print("fall")
