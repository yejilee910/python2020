# input을 이용하여 이름, 신장, 체중을 입력 받은 후 적정 평균 체중을 구하는  프로그램을 작성하시오.
#
# 적정 평균 체중 계산식 = (신장 - 100) * 0.9 ;
# 적정 평균 체중 오차는 ± 5 이며 방문자자 입력한 체중이 적정 체중일경우에는 "OOO님은 적정 체중입니다" 를, 아닐 경우에는 "OOO님은 적정 체중이 아닙니다" 를 출력하시오.
#
# 작성 과정.
# 변수 3개 만들고
# input를 이용하여 3번 값을 입력 받는다. 입력 받은 신장과 체중은 숫자로 형변환 한다.
# 표준 출력을 이용하여 결과를 화면에 출력한다.

name=input("이름을 입력하세요 : ")
height=input("신장을 입력하세요: ")
weight=input("체중을 입력하세요: ")
height=float(height)
weight=float(weight)
average = (height-100)*0.9

if weight>=average-5 and weight<=average+5 : 
    print(name,"님은 적정 체중입니다")
elif weight<average-5:
    print(name,"님은 적정 체중 이하입니다")
elif weight>average+5:
    print(name,"님은 적정 체중 이상입니다")