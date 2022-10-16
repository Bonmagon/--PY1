list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_ = 0
for i in range(len(list_numbers)):
    if max_ < list_numbers[i]:
        max_ = list_numbers[i]
        k = i
c = list_numbers[len(list_numbers)-1]
list_numbers[k] = c
list_numbers[len(list_numbers)-1] = max_

print(list_numbers)
