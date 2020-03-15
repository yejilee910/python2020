# 파티에 참석한 사람들의 명단이 세트 A와 B에 각각 저장되어 있다.
# 2개 파티에 모두 참석한 사람들의 명단을 출력하려면 어떻게 해야할까?

A = []
B = []
while True : 
    Aname = input("A파티에 참석한 사람을 입력하세요.")
    if Aname != "" : 
        A.append(Aname)
        partyA = set(A)
    else : 
        break

while True : 
    Bname = input("B파티에 참석한 사람을 입력하세요.")
    if Bname != "" :
        B.append(Bname)
        partyB = set(B)
    else : 
        break
overlap = partyA.intersection(partyB)
str = "2개의 파티에 참석한 모든 사람은 다음과 같습니다."
print(str, overlap)
