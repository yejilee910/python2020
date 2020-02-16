first = input("첫번째수를 입력하세요.")
second = input("두번째수를 입력하세요.")
third = input("세번째수를 입력하세요.")

first=int(first)
second=int(second)
third=int(third)

if (first>=second) and (first>=third) :
    print (first)
elif (first<=second) and (second>=third):
    print (second)
else:
     print(third)
###################


first = input("첫번째수를 입력하세요.")
second = input("두번째수를 입력하세요.")
third = input("세번째수를 입력하세요.")

first=int(first)
second=int(second)
third=int(third)

if (first > second) : #first와 second 비교 
    if (first > third) :
        print ("the largest is ",first)
    else : 
        print("the largest is ", third)

else : 
    if (second>third):  # second와 third 비교
        print("the largest is", second)
    else :
        print("the largest is", third)
        


