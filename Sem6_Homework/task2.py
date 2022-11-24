# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности.

import random

random.seed(165)
lst = [random.randint(0, 10) for i in range(12)]
set_lst = set(lst)

unique = [x for x in set_lst if lst.count(x) == 1]
doubles = [x for x in set_lst if not x in unique]

print('\nПоследовательность чисел:', *lst)
print('Уникальные элементы:     ', *unique)
print('Повторяемые элементы:    ', *doubles)
print('Список без дубликатов:   ', *set_lst, '\n')
