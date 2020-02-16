#항공사에서는 짐을 부칠 때, 20kg이 넘어가면 20,000원을 내야한다고 하자. 20kg 미만이면 수수료는 없다. 사용자로부터 짐의 무게를 입력받고
#사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성해보자.

weight=input("Lugguage weight : ")
weight=float(weight)

if weight>=20 : 
    print("KRW 20,000 will be charged as extra")
else :
    print("No extra charge")
