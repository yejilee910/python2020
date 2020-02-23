answer = 87
count = 0
print("1부터 100 사이의 숫자를 맞추시오")
while True:
    number = int(input("숫자를 입력하시오: "))
    if number > answer:
        print("높음!")
        count = count+1
    if number < answer:
        print("낮음!")
        count = count+1
    if number == answer:
        count = count+1
        print("축하합니다.시도횟수=", count)
        break
