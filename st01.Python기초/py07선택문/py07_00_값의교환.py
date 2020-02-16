#두 개의 수 x와 y의 초기 값이 각각 10과 20으로 주어질 때, x와 y를 서로 교환하여 출력하는 프로그램을 작성하시오.
x=input("x:")
y=input("y:")
x_original=x
y_original=y
y=x_original
x=y_original
print("교환 전",x_original,y_original)
print("교환 후",x,y)
