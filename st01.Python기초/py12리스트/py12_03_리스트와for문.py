# 리스트의 선언
numbers = []

numbers = [0, 1, 2, 3, 4, 5]  # 리스트에 값을 대입

for i in range(0, 6, 1):  # for문을 사용하여 리스트에 값을 대입
    numbers[i] = i*10
print(numbers)
# 표준입력 리스트에 저장하기
grade = []
for i in range(5):
    grade.append(int(input("성적을 입력하시오: ")))
print("성적:", grade)
total = sum(grade)
count = len(grade)
average = total/count
print("평균 성적 :", average)

# for문을 사용하여 리스트의 값 출력
for i in numbers:
    print(i)
# 리스트와  for 문
for i in range(0, len(numbers)-1, 1):
    val = numbers[i]
    print(val)

# 문자열과 for 문
for i in "안녕하세요":
    print(i)
