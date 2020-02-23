# 사용자로부터 입력받은 숫자에 해당하는 구구단을 역순으로 출력하는 프로그램을 만드시오.

number = int(input("Number : "))
print("Result: ")
for x in range(9, 0, -1):
    str = " %d * %2d = %3d" % (number, x, x*number)
    print(str)
