# 클로저 함수
# 함수를 리턴하는 내부 함수
# 내부 함수는 외부 함수의 지역 변수나 매개변수에 접근할 수 있다.


def outer_func(tag):  # 1
    text = "Some text"  # 5
    tag = tag  # 6

    def inner_func():  # 7
        return "<%s> %s </%s>" % (tag, text, tag)  # 9

    return inner_func  # 8


h1_func = outer_func("h1")  # 2
p_func = outer_func("p")  # 3

print(h1_func())  # 4
print(p_func())  # 10
