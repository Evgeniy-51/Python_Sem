# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = [2, 3, 4, 5, 6]

print([lst[i] * lst[len(lst)-i-1]
       for i in range((len(lst) + 1) // 2)])
