# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

val = input("Введите вещественное число:  ")

res = sum([int(x) if x.isdigit() else int(x.replace(x, '0')) for x in val])

print(f'Сумма цифр числа =  {res}')
