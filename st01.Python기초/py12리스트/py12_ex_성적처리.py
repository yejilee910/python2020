#학생들의 성적을 처리하는 프로그램을 완성시켜보자. 사용자로부터성적을 입력받아서 리스트에 저장한다. 
# 성적의 평균을 구하고 80점이상 성적을 받은 학생의 숫자를 계산하여 출력해보자.

print("입력을 종료하려면 엔터")
grades=[]
while True : 
    n = input("성적을 입력하시오: ")
    if n != "" : 
        n=int(n)
        grades.append(n)
    else:
        break

total = sum(grades)
count = len(grades)
average = total / count
print("평균은", average, "점 입니다.")
e=[]
for i in grades : 
    if i >= 80 : 
        e.append(i)

print("80점 이상의 성적을 받은 학생은",len(e),"명 입니다.")

