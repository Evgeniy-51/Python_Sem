# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

import math

n = int(input("Введите число N:  "))

print([math.factorial(x) for x in range(1, n + 1)])
