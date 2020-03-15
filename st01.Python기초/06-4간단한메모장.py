import sys

option = sys.argv[1]

if option == '-a' : 
    memo = sys.argv[2]
    f = open("/Users/yejilee/Downloads/python주말수업/python2020/st01.Python기초/memo.txt", "a")
    f.write(memo)
    f.write('\n')
    f.close()
elif option 