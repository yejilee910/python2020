# 10개의 정수를 입력 받아 리스트에 저장하고 이 리스트의 최대, 최소값을 구하시오.


def main():
    a = input("INPUT:")
    str_list = a.split(" ")

    num_list = []
    i = 0
    for i in range(0, len(str_list), 1):
        num = int(str_list[i])
        num_list.append(num)
        i += 1
    b = num_list
    print("리스트 정렬 전 :", b)
    c = sorted(num_list)
    print("리스트 정렬 후 :", c)
    print("최소값:", min(num_list))
    print("최대값", max(num_list))


if __name__ == "__main__":
    main()
