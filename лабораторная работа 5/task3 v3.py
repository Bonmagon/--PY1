import random


def get_unique_list_numbers(n1, n2, n3) -> list[int]:
    list_ = []
    if n2-n1 < n3:
        print("Невозможно построить лист")
        return list_
    else:
        while len(list_) != n3:
            s = random.randint(n1, n2)
            if s not in list_:
                list_.append(s)
        return list_


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
