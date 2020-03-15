# GUI 모듈
#   turtle
#   tkinter <- 리눅스 tk/tcl 언어를 파이썬으로 포팅


from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readfile = askopenfilename()

# 파일존재여부확인
if readfile != None:
    infile = open(readfile, "r", encoding="UTF-8")  # 파일 열기

    for line in infile.readlines():
        line = line.strip()  # .strip() 양쪽에 공백 제거
        print(line)

infile.close()
