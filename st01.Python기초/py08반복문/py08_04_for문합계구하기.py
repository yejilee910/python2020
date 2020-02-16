# 0부터 9까지의 합계를 구하시오
sum=0 #합계를 위한 variable지정 
for x in range(0,10,1): #x라는 값이 0~9까지 1씩 올라가며 반복하도록 
    sum=sum+x  # 기존의 sum 에 x를 더하는 행위를 순차적으로 반복 -> x=9까지 
print("sum=",sum)


# 0부터 100까지 짝수의 합계를 구하시오
total = 0
for a in range(0,102,2):
    total = total + a
print("total = ", total)
