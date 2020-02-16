A=input("A:")
B=input("B:")

try:
    A=int(A)
    B=int(B)    
    AVG=(A+B)/2
except ValueError:
    pass

if AVG == NameError :
    print("유효한 값을 입력하세요")
elif AVG >= 160 : 
    print("합격")
else :
    print("불합격")
