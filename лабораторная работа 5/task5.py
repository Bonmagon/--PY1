import random


def get_random_password(n=8) -> str:
    str_ = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
    pas = ""
    for i in random.sample(str_, n):
        pas += i
    return pas


print(get_random_password())
