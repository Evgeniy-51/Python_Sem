# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from decimal import *

lst = [1.1, 1.2, 3.1, 5.0001, 10.01]
min, max = 1, 0

for elem in lst:
    elem = str(elem)
    elem = elem.split('.') if '.' in elem else ['0', '0']
    fract_part = int(elem[1])/10**len(elem[1])
    if fract_part > max:
        max = fract_part
    if fract_part < min:
        min = fract_part

print(f"\nMin = {min}, Max = {max}")
print(f"Разница = {Decimal(str(max)) - Decimal(str(min))}")
