# 중첩 for문
for x in range(2, 10, 1):
    for y in range(1, 10, 1):
        print("%s * %s = %2s" % (x, y, x*y), end=",")
    print()
