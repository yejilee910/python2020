#직사각형의 넓이와 둘레를 구하는 프로그램을 작성한다. 
#직사각형의 가로와 세로를 각각 w와 h라고 하면 직사각형의 넓이는 w*h가 되고 둘레는 2*(w+h)가 된다 
#w와 h 값은 input()을 사용하여 입력 받아 계산하시오. 

try:
    w=float(input("직사각형의 가로 길이를 입력하세요: ")) #float는 문자를 실수(소수점까지)로 변환하는 함수 int는 소수점 날리고 정수만 표기 
    h=float(input("직사각형의 세로 길이를 입력하세요: "))
except ValueError:
    pass
area=w*h
print("직사각형의 넓이:",area)
perimeter=2*(w+h)
print("직사각형의 둘레:", round(perimeter,2)) #round는 반올림 함수
