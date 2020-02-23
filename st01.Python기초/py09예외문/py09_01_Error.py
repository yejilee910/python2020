
# 숫자가 아닌 것을 정수로 변환하려고 할 때

# 숫자가 아닌 것을 실수로 변환 할 때

# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환하려고 할 때

# IndexError

try:
    x = int(input("Please enter a number : "))
    print(x)
except ValueError as identifier:
    print("Oops! That was no valid number. Try again....")
