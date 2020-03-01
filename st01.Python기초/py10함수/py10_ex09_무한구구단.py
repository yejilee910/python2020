# 시작 단수와 종료 단수를 입력 받고, 해당 단에 해당하는 구구단을
# 출력하는 프로그램을 작성하시오.

# 시작단이 종료단보다 큰 경우에도 가능하게 하시오.
# 출력은 작은단부터 큰단 순으로 구구단을 출력하시오.

# 입력 받는 정수에 0 이 있는 경우에만 프로그램을 종료하고
# 아니면 계속 새로운 시작단과 종료단를 입력 받아 출력하게 하시오


def gugudan(start, end):
    while True:
        if start != 0 and end != 0:
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
        break


def main():
    while True:
        start = int(input("시작 단수를 입력하세요 : "))
        end = int(input("종료 단수를 입력하세요 : "))
        if start != 0 and end != 0:
            gugudan(start, end)
        elif start == 0 or end == 0:
            print("종료")
            break


if __name__ == "__main__":
    main()
