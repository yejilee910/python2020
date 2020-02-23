
str = input("값을 입력하세요")
while True:
    try:
        a = int(str)
        sen="%d * 10 = %d" % (a, 10*a)
        print(sen)
    except ValueError as identifier:
        print("error")
    break
