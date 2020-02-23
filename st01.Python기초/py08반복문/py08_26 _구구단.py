start = int(input("시작 단수를 입력하세요 : "))
end = int(input("종료 단수를 입력하세요 : "))
if start > end:
    temp = start
    start = end
    end = temp
else:
    pass

for x in range(start, end+1, 1):
    for y in range(1, 10, 1):
        if y == 9:
            str = "%2s*%s=%3s" % (x, y, x*y)
            print(str, end=".")
            print()
        else:
            str = "%2s*%s=%3s" % (x, y, x*y)
            print(str, end=",")
