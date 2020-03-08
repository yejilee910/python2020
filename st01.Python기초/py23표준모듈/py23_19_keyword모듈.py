import keyword

name = input("변수 이름을 입력하시오. :")

if keyword.iskeyword(name):
    print(name, "은 이미 사용중인 키워드(예약어)임..")
    print("아래 키워드는 전체 리스트임.")
    print(keyword.kwlist)
else:
    print(name, "은 사용할 수 있는 변수이름임")
