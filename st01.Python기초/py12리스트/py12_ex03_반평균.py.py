
# 1. List 만들기.
# 2. 학생수 입력 받기. 최소 3명이상
# 3. 학생 성적 입력 받기. 몇번 입력받아야 하는가?
# 4. list에 입력 받은 학생 성적을 추가한다.
# 5. 3번 학생의 성적을 100점으로 바꾸시오.
# 6. list에서 마지막 학생 삭제.
# 7. list에서 0번 값을 출력하시오.
# 8. 평균을 구하고 출력.


students = int(input("학생수를 입력하시오: "))
i = 0
grade_list = []
for i in range(1, students+1, 1):
    grade = int(input("성적을 입력하시오:"))
    grade_list.append(grade)
    i += 1
total = sum(grade_list)
count = len(grade_list)
average = total / count
print("합계는:", total)
print("평균은:", average)
