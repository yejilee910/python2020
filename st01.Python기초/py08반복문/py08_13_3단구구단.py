
#while문을 이용한 3단 출력
i = 1
while i <= 9 : 
    str = "i=%d, %d * %d = %2d" % (i, 3, i, 3*i)
    print(str)
    i = i +1
print ("while문 종료")