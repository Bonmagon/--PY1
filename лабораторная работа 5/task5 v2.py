import random
import string


def get_random_password(n=8) -> str:
    str_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    pas = ""
    for i in random.sample(str_, n):
        pas += i
    return pas


print(get_random_password())
