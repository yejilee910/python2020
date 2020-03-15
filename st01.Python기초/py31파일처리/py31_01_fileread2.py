import os.path

infile = open(
    "/Users/yejilee/Downloads/python주말수업/python2020/st01.Python기초/py31파일처리/file/phones.txt", "r")
s = infile.readline()
print(s, end="")
s = infile.readline()
print(s, end="")
s = infile.readline()
print(s, end="")
infile.close()
