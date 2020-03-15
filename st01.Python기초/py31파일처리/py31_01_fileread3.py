import os.path

infile = open("/Users/yejilee/Downloads/python주말수업/python2020/st01.Python기초/py31파일처리/file/phones.txt", "r")
line = infile.readline()
while line != "":
    print(line, end="")
    line = infile.readline()
infile.close()
