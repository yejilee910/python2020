# 입력 파일 이름과 출력 파일 이름을 받는다.
# 입력과 출력을 위한 파일을 연다.
import os.path

infile = open(
    "/Users/yejilee/Downloads/python주말수업/python2020/st01.Python기초/py31파일처리/file/sales.txt", "r", encoding="UTF-8")
outfile = open(
    "/Users/yejilee/Downloads/python주말수업/python2020/st01.Python기초/py31파일처리/file/summary.txt", "w")

# 합계와 횟수를 위한 변수를 정의한다.
sum = 0
num = 0
# 입력 파일에서 한 줄을 읽어서 합계를 계산한다.
for sale in infile.readlines():
    sale = sale.strip()
    sale = float(sale)
    num += 1
    sum += sale

average = sum / num

str1 = "총매출 = "
str2 = "평균 일매출 ="

# 총매출과 일평균 매출을 출력 파일에 기록한다.

outfile.write(str1 + "%s" % sum)
outfile.write("\n")
outfile.write(str2 + "%.1f" % average) 

infile.close()
outfile.close()
