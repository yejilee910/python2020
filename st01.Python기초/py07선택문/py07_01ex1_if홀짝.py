# 정수를 입력을 받습니다.
# 입력 받은 문자열을 정수로 바꿉니다.
number=input("정수를입력하세요:")
number=int(number)
# 문자열로 변환
number=str(number)
#######################################
# 방법1. 문자열을 사용하는 방법
# 방법2. 나머지를 사용하는 방법
#######################################

#######################################
# 방법1. 문자열을 사용하는 방법
#######################################
# 마지막 자리 숫자를 추출
number=number[len(number)-1:]
# 숫자로 변환하기
number=int(number)
# 짝수 확인
if number%2==0:
    print("짝수")
# 홀수 확인
if number%2==1:
    print("홀수")




#######################################
# 방법2. 나머지를 사용하는 방법
#######################################

# 짝수 조건
number=input("정수를입력하세요:")
number=int(number)
if number%2==0 : 
    print("짝수입니다")
# 홀수 조건
number=input("정수를입력하세요:")
number=int(number)
if number%2==1 : 
    print("홀수입니다")


#또다른 홀수, 짝수 판별법
#입력된 값의 마지막 글자만을 추출하여 홀수 짝수를 판별
number=input("마지막글자용:")
number=number[len(number)-1:]

if number ==0 \
    or number ==2 \
        or number ==4 \
            or number == 6\
                or number == 8:
                print("짝수")
else :
    print("홀수")

