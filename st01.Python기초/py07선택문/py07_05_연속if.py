# py04_02_ifelse

# 하나의 점수를 입력 받고, 입력 받은 점수에 해당하는 학점을 출력하는 프로그램을 작성하시오.
# 입력 받는 정수는 0~100까지이고    
# 90점 이상이면 A,    
# 80점 이상이면 B,    
# 70점 이상이면 C,   
# 60점 이상이면 D,    
# 나머지는 F

grade=float(input("Grade:"))
if grade >= 90 : 
    print("학점:A")
elif grade< 90 and grade>=80 : 
    print("학점:B")
elif grade < 80 and grade >= 70 :
    print("학점:C")
elif grade >= 60 :
    print("학점:D")
else :
    print("학점:F")

#코딩은 순차적으로 위-> 아래순으로 조건을 돌리기 때문에 순차적으로 조건을 잡는 다면 굳이 구간(이상~이하)으로 잡을 필요없음 
grade=float(input("Grade:"))
if grade >= 90 : 
    print("학점:A")
elif  grade >=80 : 
    print("학점:B")
elif grade >= 70 :
    print("학점:C")
elif grade >= 60 :
    print("학점:D")
else :
    print("학점:F")