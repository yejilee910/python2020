# 파일 존재 유무 및 파일 경로 확인
import os

print("현재 경로 : ", os.getcwd())

#########################
# readline() 파일에서 한 줄씩 읽기
infile = open("./py31파일처리/file/phones.txt", "r", encoding="UTF-8")
s = infile.readline()
print(s, end="")
s = infile.readline()
print(s, end="")
s = infile.readline()
print(s, end="")
infile.close()
print("---반복문으로처리하기---")
# 반복문으로 처리하기
infile = open("./py31파일처리/file/phones.txt", "r", encoding="UTF-8")
line = infile.readline()
while line != "":
    print(line, end="")
    line = infile.readline()
infile.close()


print("#########################")
infile = open("./py31파일처리/file/phones.txt", "r")
s = infile.read(10)
print(s, end="")
infile.close

#########################
##
