# 문자열은 수정 불가
# 새로 메모리가 할당되는 것이지 기존의 메모리가 수정되는 것이 아님

str1 = "abc"
print('str1 address', id(str1))
print()
str2 = str1
print("str2 address", id(str2))
print()
str1 = "efg"
print("new str1 address", id(str1))
print()
