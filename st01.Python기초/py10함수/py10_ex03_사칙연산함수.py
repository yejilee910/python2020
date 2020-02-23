
x = input("First num : ")
y = input("Secone num: ")

x = int(x)
y = int(y)


def add(x, y):
    result = x + y
    return result


def Div(x, y):
    result = float(x/y)
    return result


def Minus(x, y):
    result = x-y
    return result


def Mul(x, y):
    result = x*y
    return result


value = add(x, y)
print("Add : ", value)

value = Minus(x, y)
print("Minus : ", value)

value = Mul(x, y)
print("Mul : ", value)

value = Div(x, y)
print("Div : ", value)
