#  Вычислить число c заданной точностью d

from decimal import *

num = input("Введите число с плавающей запятой: ")
d = input("Введите формат округления числа: ")

print(Decimal(num).quantize(Decimal(d)))
