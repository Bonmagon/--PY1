def delete(list_, index = None):
    if index == None:
        index = len(list_) - 1
    list_a = list_[:index]
    list_b = list_[index+1:]
    result = list_a + list_b
    return result


print(delete([0, 0, 1, 2], index=1))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
