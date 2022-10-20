# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

num = int(input('\nEnter a number: '))
lst = [0, 1]
k = -1

for i in range(2, num*2, 2):
    elem = lst[i-1] + lst[i-2]
    lst.insert(0, elem*k)
    lst.append(elem)
    k *= -1

print(lst)
