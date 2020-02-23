
# 1부터 10까지의 합계를 구하고
# 그 합계를 sum에 저장하고 sum 값을 한번만 출력한다.
sum = 0
for a in range(1, 11, 1):
    sum = sum+a
print(sum)

# 1부터 100까지의 합계를 구하고
# 그 합계를 sum2 에 저장하고 sum2 값을 한번만 출력한다.
sum2 = 0
for b in range(1, 101, 1):
    sum2 += b
print(sum2)

# 100부터 sum2까지의 합계를 구하고
# 그 합계를 sum3 에 저장하고 sum3 값을 한번만 출력한다.
sum3 = 0
for c in range(100, sum2+1, 1):
    sum3 += c
print(sum3)


# 반복되는 코드를 함수로 만들어 사용
# 함수에서 바뀌는 값은 입력(매개 변수)로 처리한다.
# 매개 변수=parameter
def get_sum(x, y):
    total = 0
    for i in range(x, y+1, 1):
        total = total + i
    return total


total1 = get_sum(1, 10)
total2 = get_sum(1, 100)
print(total1, "&", total2)

