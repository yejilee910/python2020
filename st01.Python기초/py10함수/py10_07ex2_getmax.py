# ����� �Լ� �����
# �� ���� ������ �־����� �μ� �߿��� �� ū ���� ã�Ƽ� �̰��� ��ȯ�ϴ� �Լ��� ������. 

def getmax(x , y) :
    result = None # None 은 값이 없음(nill)을 의미 
    if x > y : 
        result =  x
    else : 
        result = y
    return result 

print(getmax(2,10))
#왜 main() 함수를 사용하는가? 
#프로그래밍에서는 전역변수를 사용하지 않는 것을 권장함. 전역변수 = 함수 안에서 정의되지 않는 변수 
#입력처리
def main(): 
n1 = input ("첫번째 정수 입력 : ")
n1 = int(n1)

n2 = input ("두번째 정수 입력 : ")
n2 = int(n2)

def val(n1, n2) : 
return n1*n2



# def myinput(message) : 
#  try : 
#     n1 = input(message)
#     n1 = int(n1)
# except ValueError as ex : 
#     print ( ex )
# return n1 


