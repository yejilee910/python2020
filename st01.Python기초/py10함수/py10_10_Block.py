
def get_sum(x, y):  # x,y 매개변수
    total = 0
    for i in range(x, y+1, 1):
        total = total + i
    return total

    # 함수 호출
a = 3  # 전역변수
b = 7  # 전역변수
value = get_sum(a, b)
print(value)

# 변수의 종류
# 전역 변수 : 함수 문 내부에 존재하지 않는 모든 변수 -> 함수에서 접근이 가능 
# 지역 변수 : 특정 함수 내부에만 존재 
# 매개 변수 : 함수 문 내부 

