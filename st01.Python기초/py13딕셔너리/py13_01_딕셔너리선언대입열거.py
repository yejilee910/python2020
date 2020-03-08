# 딕셔너리의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle

# 딕셔너리 선언하기
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "소금", "치자"],
    "origin": "필리핀"
}

# 요소 추가 전에 내용을 출력해봅니다.
print("name: ", dictionary["name"])
print("type: ", dictionary["type"])
print("ingredient: ", dictionary["ingredient"])
print("origin: ", dictionary["origin"])
print()

a = dictionary.get("name")
b = dictionary.get("ingredient")
print(a, b)

# 딕셔너리 추가
dictionary["head"] = "머리"  # '머리'라는 value를 가진 'head' 'key'를 dictionary에 추가
dictionary["body"] = "몸"

# 선택 연사자[]로 딕셔너리 읽기
# dictionary의 head의 값을 출력하시오.
print("value of \'head\' is ", dictionary.get("head"))
print("value of \'head\' is ", dictionary["head"])

# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생.
# dictionary["존재하지 않는 키"] # KeyError
# try-except 걸어서 에러 방지
try:
    a = dictionary.get("존재하지 않는 키")
    print(a)
except KeyError as ex:
    print(ex)

# 딕셔너리 수정
# namedml value를 8D망고로 수정하기
print("name", dictionary["name"])
dictionary["name"] = "8D 망고"
print("new \'name\'", dictionary["name"])


# 딕셔너리 삭제.
# 1. 연산자 방식 : del. 비추천
# 2. 메서드 방식 : .pop("key") 추천
# 3. 다 지워버리는 것 .clear() method 사용
# name, type 키를 삭제
print("삭제 전", dictionary)
dictionary.pop("name")
dictionary.pop("type")
print("삭제 후", dictionary)


# 존재하지 않는 키에 접근하면 에러 발생. try~except 를 추가하시오.
# 딕셔너리 키 존재 여부 확인 => .get() 메서드 사용
# value = dictionary["존재하지 않는 키"]  의 경우 None을 반환
# value가 None이면 키가 없다는 의미
# 키가 존재하지 않는 경우의 확인 방법 :  None 사용
# 출력합니다.
#a = input("키를 입력하시오")
value = dictionary.get(a)
if value == None:
    print("Key does not exist in dictionary")
else:
    print("Key exists")
    print(value)

if "존재하지 않는 키" in dictionary:
    print("키 값이 존재한다")
    print(dictionary["존재하지 않는 키"])
else:
    print("키가 존재하지 않는다")

print()

a = {
    "name": "Fay",
    "phone": "01011112222",
    "birth": "1118"
}
"name" in a  # True
"email" in a  # Fale

if "name" in a:
    print("Her name is ", a["name"])


# dictionary를 정렬하는 방법은 없음(리스트와의 차이점),
# 단, Key값만 정렬하는 것은 가능. value값만 정렬하는 것은 가능


# 딕셔너리 열거

# key 만 열거 - .keys() 메서드 사용
for key in dictionary.keys():
    print("keys >>>", key)

# value 만 열거 - .values() 메서드 사용
for value in dictionary.values():
    print('values >>>', value)
# key, value를 쌍으로 열거 - .items() 메서드 사용
for item in dictionary.items():
    print("items >>>", item)
