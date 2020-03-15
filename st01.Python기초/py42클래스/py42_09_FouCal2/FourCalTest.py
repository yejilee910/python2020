
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기

class Car() :
    def __init__(self, speed = 0, gear = 1, color = "white") : 
        this.color = "red";
        this.speed = 0 ; 
        this.gear = 1 ;
    
    def speedUp(self, s) : 
        self.speed += s ;
    
    def speedDown(self, s) :
        self.speed -= s ; 
    
    def speedPrint(self) :
        print("속도" + self.speed + "km")

