flag = True 
print(flag)

flag = (2>3)
print(flag)

print(True)
print(False)
print("---------")
print(10 == 100)
print(10 != 100)
print(10<100)
print(10>100)
print(10<=100)
print(10>=100)
print("----------")
print("가방"=="가방")
print("가방" != "하마")
print("-----------")
#글자의 비교 연산 기준은 사전 순으로 이해 (ㄱ =1, ㄴ=2, ㄷ=3 식으로 뒤에 있을 수록 큰 것으로 인식)
#문자열 간 비교 연산 가능 
print("가방"<"하마") #True
print("가방">"하마") #False

print("--------")
x = 25
print(10<x<30) 
print(10<x and x<30) #파이선을 제외한 다른 언어는 이러한 형식으로 표기해야 함 
print(40<x<60) #false
