
# 2단의 구구단을 가로 출력하는 프로그램을 만드시오. 끝날 때는 마침표를 붙인다.
# 힌트. 출력할 문자열을 변수에 저장하고 마지막 한번만 변수값을 print()를 사용하야 출력해야 한다.

for x in range(1, 10, 1):
    print("2*", x, "=", 2*x, end=",")
print(".")


for x in range(1, 10, 1):
    str = "2 * %d = %2d" % (x, 2*x)
    # x가 9이면 마침표를 찍고 아니면 콤마를 찍어라
    if x == 9:
        print(str, ".")
    else:
        print(str, ",")


for x in range(1, 10, 1):
    str = "2 * %d = %2d" % (x, 2*x)
    if x == 9:
        print(str, end=".")
    else:
        print(str, end=", ")
