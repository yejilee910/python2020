import os.path


def main():

    outfile = open(
        "/Users/yejilee/Downloads/python주말수업/python2020/st01.Python기초/py31파일처리/file/phones.txt", "a", encoding="UTF-8")
    print(outfile)
    if os.path.isfile("phones.txt"):
        print("동일한 이름의 파일이 이미 존재합니다.")
    else:
        outfile.writelines("김길동 010-1234-5678 \n")
        outfile.writelines('김철수 010-1234-5677')
        outfile.writelines("김영희 010-1234-5680")

    outfile.close()


if __name__ == "__main__":
    main()
