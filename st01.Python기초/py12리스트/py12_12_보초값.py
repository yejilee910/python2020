print("종료하려면 음수를 입력하시오")
grade=[]
while True:
    n = int(input("성적을 입력하시오: "))
    if n >= 0:
        grade.append(n)
    else :
        break

total = sum(grade)
count = len(grade)
average = total / count
str = "성적의 평균은 %s 입니다" % average
print(str)
    