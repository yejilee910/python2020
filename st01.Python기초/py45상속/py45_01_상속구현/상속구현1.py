
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. Parent 부모 클래스를 선언합니다.
# 3. Child 자식 클래스를 선언합니다. 부모 자식 관계 설정 하는 것이 중요.
# 4. main() 메서드 만들기
#     자식 클래스의 인스턴스를 생성하고 부모의 메서드를 호출합니다.
# 5. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()


# 코딩 하기

# Parent Class 생성하기

class Parent():
    def __init__(self):
        self.__value = "parent variant"

    def test(self):
        print("Parent 클래스의 test() method입니다.")

    def getValue(self):
        return self.__value

# Child Class 생성하기


class Child(Parent):
    def __init__(self):
        self.__value = "Child variant"

# child class는 test() method가 없음. parent의 test() method를 child도 자유자재로 쓸 수 있도록 하자


child = Child()
child.test()
parent = Parent()
parent.getValue()
