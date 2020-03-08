# 현대인들은 축약어를 많이 사용한다. 예를 들어서 "B4(Before)" "TX(Thanks)" "BBL(Be Back Later)" "BCNU(Be Seeing You)" "HAND(Have A Nice Day)"와 같은 축약어들이 있다.
# 축약어를 풀어 서 일반적인 문장으로 변환하는 프로그램을 작성하여 보자.

# 작업순서
# 문자열을 split() 해서 array 리스트로 만든다.
# 반복문을 사용하여 array 리스트를 루프를 돌면서 딕셔너리 table에 찾는다. table에서 찾을 때는 .get() 메서드나 in 연산자를 사용
# 찾았다면 바꾼다 .replace()
# 출력한다. 문자열 메서드 join() 을 사용하는 것으로 작성


table = {
    "B4": "Before",
    "TX": "Thanks",
    "BBL": "Be Back Later",
    "BCNU": "Be Seeing You",
    "HAND": "Have A Nice Day"
}
sentence = input("번역할 문장을 입력하시오 : ")
array = sentence.split()  # split() 메서드를 쓰면 알아서 리스트로 결과가 생성됨
result = ""
for i in array:
    value = table.get(i)
    if value != None:
        sentence = sentence.replace(i, value)
        result = sentence 
    else:
        result = sentence

print(result)

