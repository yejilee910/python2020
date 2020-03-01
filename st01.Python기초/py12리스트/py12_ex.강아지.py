dogs = []
while True:
    d = input("강아지 이름을 입력하세요(종료시에는 엔터키): ")
    if d != "":
        dogs.append(d)
    else:
        break

print("강아지들의 이름 \n", dogs)
print("총 강아지의 수는",len(dogs), "마리")

