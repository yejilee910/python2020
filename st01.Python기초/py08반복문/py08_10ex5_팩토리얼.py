# 팩토리얼을 계산하는 프로그램
# 팩토리얼 n! = 1*2*3*...*(n-1)*n

n = int(input("정수를 입력하시오 : "))
pec = 1
for x in range(n, 0, -1):
    pec = pec*x
print("10!은 ", pec, "이다")
