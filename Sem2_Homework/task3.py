# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

n = int(input("Введите количество чисел:  "))

print(sum([(1 + 1 / x) ** x for x in range(1, n+1)]))
