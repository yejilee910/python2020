x = 3
y = 4

r = ((x==3) and (y==3)) #True and False => False    
print("1.(x==3) and (y==3) :", r)

r = ((x==3) and (y != 3)) #True and True
print("2.(x==3) and (y!=3):", r)

r=((x ==3) or (y == 3)) #True or False => False
print("3.(x==3) or (y==3):",r)

r=((x==3) or (y==4)) # Ture or True 
print("4.(x==3) or (y==4):", r)

r=((x!=3) or (y==4)) # False or True => False 
print("5.(x!=3) or (y==4):", r)

r=((x!=3) or (y!=4)) #False or False = false
print("6.(x!=3) or (y!=4):",r)

print("----------")
x=3
y=4
print((x==y)and(x !=y)) #false and true 
print((x>y)or(x<y))
print((x>=y)or(x<=y))
print((x==y)and (x !=y) or (x<y)) # true and false = true / true or true = true