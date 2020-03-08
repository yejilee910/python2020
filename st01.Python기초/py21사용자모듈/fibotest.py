# import 방식
# 1.모듈 import : import 모듈이름


from fibo import *
import fibo


def main():
    #사용방법 ; 모듈명.함수명
    n = input("숫자를 입력하세요 : ")
    n = float(n)
    result = fibo.fib2(n)
    print(result)


# 2.함수 import : from 모듈이름 import 모율함수
fib2(500)
print(fib2)
# 3. as import


# 이 모듈이 단독으로 사용되면 main()를 호출하라.

if __name__ == "__main__":
    main()
