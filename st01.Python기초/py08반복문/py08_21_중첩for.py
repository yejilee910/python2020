# 중첩 for문

# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********

for i in range(0, 10, 1):
    print("***********")
print("-------------")

for a in range(0, 10, 1):
    for j in range(0, 10, 1):
        print("*", end="")
    print()  # 줄바꿈을 위해 for문 밖에 print()를 추가

print("---b-----")

for y in range(1, 11, 1):
    for x in range(1, y+1, 1):
        print("*", end="")
    print()
# y가 1이면 x는 1부터 1까지 *를 찍는다
# y가 2이면 x는 1부터 2까지 *를 출력
print("----c--------")
for y in range(1, 11, 1):
    for x in range(1, y+1, 1):
        print(" ", end="")
    for x in range(y+1, 11, 1):
        print("*", end="")
    print()
# y가 1일때 1부터 1부터 1까지 빈칸, 2부터 10까지는 * 출력
