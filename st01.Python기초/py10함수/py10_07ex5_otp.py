# ����� �Լ� �����
# ��ȸ�� �н����� �����⸦ �̿��Ͽ��� 3���� �н����带 �����Ͽ� ����ϴ� ���α׷��� �ۼ��غ���.

import random


def genPass():
    alphabet = "abcdefghijklmnopqrstuvsxyz0123456789"
    password = ""

    for i in range(6):
        index = random.randrange(len(alphabet))
        password = password + alphabet[index]
    return password


print(genPass())
print(genPass())
print(genPass())
