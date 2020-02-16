#2단의 구구단을 출력하는 프로그램을 만드시오

for x in range(1,10,1):
    print("2*",x,"=",2*x)

#formatting을 사용해서 두자리수로 맞추기 
for x in range(1,10,1):
    print("2 * %d = %2d" % (x, 2*x))
