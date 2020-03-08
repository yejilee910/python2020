# 원의 넓이와 둘레를 동시에 반환하는 함수를 작성, 테스트

import math  # math.pi 를 쓰기 위해


def circle(radius): #반지름으로 원의 넓이, 둘레를 구하는 함수 생성 
    area = math.pi * radius * radius
    circum = 2 * math.pi * radius
    return (area, circum)


def main():
    str = input("원의 반지름을 입력하시오 : ")
    radius = float(str)
    (x, y) = circle(radius)  # x = area(넓이), y = circum(둘레)

    result = '원의 넓이는 %10.4f, 둘레는 %10.4f 이다.' % (x, y)
    print(result)


if __name__ == "__main__":
    main()

