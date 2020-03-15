
#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오
import os.path

proverb = open("/Users/yejilee/Downloads/python주말수업/python2020/st01.Python기초/py31파일처리/file/proverbs.txt", "r", encoding="UTF-8")
new = open("/Users/yejilee/Downloads/python주말수업/python2020/st01.Python기초/py31파일처리/file/output.txt", "w", encoding="UTF-8")

for line in proverb :
    new.writelines(line)
print("작업완료")

proverb.close()
new.close()

