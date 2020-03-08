#사용자가 지정하는 파일을 읽어서 파일에 저장된 각각의 단어가 몇번이나 나오는지를 계산하는 프로그램을 작성하여 보자.

fname = input("파일 이름 : ")
file = open(fname, "r")

table = dict() # dict() 빈 딕셔너리 생성 
for line in file : 
    words = line.split()
    for word in words : 
        if word not in table : 
            table[word] = 1
        else : 
            table[word] += 1

print(table)
