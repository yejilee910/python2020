
contact_list = []


def contact_print():
    return print(contact_list)

def contact_add(name):
    name = input("이름을 입력하시오:")
    return contact_list.apend(name)


def contact_del(name):
    name = input("이름을 입력하시오:")
    del contact_list[contact_list.index(name)]


def contact_change(n1, n2):
    n1 = input("AS-IS : ")
    n2 = input("TO-BE : ")
    contact[contact_list.index(n1)] = n2



def close():
    return print("*"*10)


contact = {"1": contact_print(), "2": contact_add(name), "3": contact_del(
    name), "4 ": contact_change(n1, n2), "9": close()}

print("-"*20)
print("1. ")