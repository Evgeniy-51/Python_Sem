# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input("\nВведите число N:  "))
lst = [random.randrange(-n, n + 1) for x in range(n)]
prod = 1
exp = []

with open('file.txt') as file:
    for i in file:
        if int(i) < n:
            prod *= lst[int(i)]
            exp.append(f'{lst[int(i)]} ({int(i)})')

print(f'\nСписок: {lst}')
print(f'\nЭлемент и (индекс): {exp}')
print(f'\nРезультат: {prod}\n')
