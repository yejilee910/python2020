# 1부터 사용자가 입력한 수 n까지 더해서 (1+2+3+...+n)을 계산하는 프로그램

n = int(input("어디까지 계산할까요: "))
sum = 0
for x in range(1, n+1, 1):
    sum = sum + x
    str = "1부터 %d 까지의 정수의 합 = %2d" % (n, sum)
print(str)
