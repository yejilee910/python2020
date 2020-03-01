# 1. List 만들기.
# 2. 학생수 입력 받기. 최소 4명이상
# 3. 학생 성적 입력 받기. 몇 번 입력 받아야 하는가?
# 4. 3번 학생의 성적을 100점으로 바꾸시오.
# 5. list에서 마지막 학생 삭제.
# 6. list에서 첫번째 값을 출력하시오.
# 7. 평균을 구하고 출력.


student = int(input("학생 수를 입력하시오: "))
if student < 4:
    student = int(input("4명 이상을 입력하세요: "))
else:
    pass
i = 0
gradelist = []
for i in range(0, student, 1):
    grade = int(input("성적을 입력하시오: "))
    gradelist.append(grade)
    i += 1

gradelist[2] = 100
del gradelist[len(gradelist)-1]
print(gradelist)
total = sum(gradelist)
count = len(gradelist)
average = total/count
print("첫번째 학생의 성적 ", gradelist[0])
print("합계는 ", total, "점")
print("평균은", average, "점")
