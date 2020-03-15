# 피타고라스의 정리를 만족하는 삼각형들을 모두 찾아보자.
# 삼각형 한 변의 길이는 1부터 30 이하이다.

result = []
for a in range (1, 31) : 
    for b in range (a, 31 ) : 
        for c in range (1, 30) : 
            if a**2 + b**2 == c**2 : 
                i = (a, b, c)
                result.append(i)

print(result)
