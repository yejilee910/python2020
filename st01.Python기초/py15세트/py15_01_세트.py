numbers = {2, 1, 3}
print(len(numbers))

fruits = {"Apple", "Banana", "Pineapple"}
myset = {1.0, 2.0, "Hello World", (1, 2, 3)}

if 1 in numbers:
    print("집합 안에 1이 있습니다.")

for x in numbers:
    print(x, end=",")

numbers.add(4)
print(numbers)
