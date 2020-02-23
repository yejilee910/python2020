# 정수 안의 각 자리수의 합을 계산하는 프로그램을 작성
# 예를 들어 1234라면 (1+2+3+4)를 계산하는 것

number = input("정수입력 :")
i = 0
sum = 0
while i < len(number):
    a = number[i]
    sum = sum+int(a)
    i = i+1
print("자리수의 합은", sum, "입니다.")
