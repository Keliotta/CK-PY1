

list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sorted_ = sorted(list_numbers)

for per in range(len(list_numbers)):
    if list_numbers[per] == sorted_[-1]:
        max_per = per
        list_numbers[max_per], list_numbers[-1] = list_numbers[-1], list_numbers[max_per]


print(list_numbers)