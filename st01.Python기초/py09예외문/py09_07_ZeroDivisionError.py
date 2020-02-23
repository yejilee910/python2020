# 무한 루프를 끝내는 ctl+c 키를 무력화시키는 예외처리

num1 = input("숫자 1 입력 : ")
num2 = input("숫자 2 입력 : ")

try:
    num1 = int(num1)
    num2 = int(num2)
    res = num1/num2
    print(res)
except ValueError as ex : # 추후 프로그밍 시 exept 형태로 Error들이 로그파일에 저장되도록 처리 가능 
    print("ValueError",ex)
except ZeroDivisionError as ex : 
    print("ZerodivisionError", ex)

