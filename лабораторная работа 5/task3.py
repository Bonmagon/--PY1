import random


def get_unique_list_numbers() -> list[int]:
    list_ = [random.randint(-10, 10) for _ in range(15)]
    while len(list_) != len(set(list_)):
        list_ = [random.randint(-10, 10) for _ in range(15)]
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
