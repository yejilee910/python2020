# 사용자로부터 임의의 개수의 성적을 받아서 평균을 계산한 후에 출력하는 프로그램
# 센티널로는 음수의 값을 사용하자.

# 방법 1
print("종료하려면 음수를 입력하시오")
grade = int(input("성적을 입력하시오: "))
gradelist = []
sum = 0
while grade > 0:
    gradelist.append(grade)
    grade = int(input("성적을 입력하시오: "))
    if grade < 0:
        number = len(gradelist)
        for a in range(0, number, 1):
            sum = sum+int(gradelist[a])
        average = sum/number
        print("성적의 평균은 ", average, "입니다.")

# 방법2
total = 0
cnt = 0
print("종료하려면 음수를 입력하시오")
while True:  # 무한루프
    g = int(input("성적을 입력하시오: "))
    if g < 0:
        break  # 특정조건일때 반복문을 종료
    else:
     cnt = cnt+1  # 입력횟수
      total =total+g
avg=total/cnt
str = "성적의 평균은 %s 입니다." % avg
print(str)


