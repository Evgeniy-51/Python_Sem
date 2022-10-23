# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

random.seed(154)
num_list = [random.randint(0, 20) for i in range(20)]
res_list = []
duplicates = []
start_pos = 0

for elem in num_list:
    is_unique = True
    start_pos += 1
    if elem in duplicates:
        continue

    for i in num_list[start_pos:]:
        if i == elem:
            is_unique = False
            duplicates.append(i)

    if is_unique:
        res_list.append(elem)


print(num_list)
print(res_list)
