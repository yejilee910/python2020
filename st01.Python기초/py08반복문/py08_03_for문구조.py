# for : 정해진 횟수만큼 반복하도록 하는 구조. -> 특정 데이터를 처리하여 열거할 때 
# Sequence : list-string / tuple / set / dictionary 
# for Variable in Sequence 

for name in ["철수", "영희", "길동", "유신"] : # list는 [ ]안에
    print ("안녕!"+ name)

for x in [1, "a", True , None, ["가"]]: 
    print(x,end=",") 
print()

for x in "abcd faoa" :
    print(x, end=",") #end="," 가 있어야 한 줄에 옆으로 