
#########################
##
#########################


# 파일을 연다.
file = open("/Users/yejilee/Downloads/python주말수업/python2020/st01.Python기초/py31파일처리/file/data.csv", "r")
# 파일 안의 각 줄을 처리한다.
for line in file.readlines() : 
    line = line.strip()    # 공백 문자를 없앤다.
    print(line)     # 줄을 출력한다.
    parts = line.split(",")     # 줄을 쉼표로 분리한다.
    for part in parts : 
        print("  ", part)    # 각 줄의 필드를 출력한다.

file.close()
