
for x in range(2, 20, 1):
    for y in range(1, 10, 1):
        str = "%2s * %s = %3s" % (x, y, x*y)
        if y == 9:
            print(str, end=".")
            print()
        else:
            print(str, end=",")
