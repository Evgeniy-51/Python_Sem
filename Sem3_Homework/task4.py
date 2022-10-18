# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

from decimal import *

# Программа работает с целыми, вещественными и отрицательными числами
dec_num = Decimal(input('\nВведите десятичное число:  '))
int_part = int(abs(dec_num))
fract_part = Decimal(abs(dec_num) - int_part)
result = '0' if int_part == 0 else ''
mark = '-' if dec_num < 0 else ''

while int_part > 0:
    rem = int_part % 2
    int_part = int_part//2
    result = str(rem) + result

if fract_part != 0:
    result += '.'
    limit = 20
    while fract_part > 0 and limit > 0:
        fract_part *= 2
        result += str(fract_part.quantize(Decimal('1'), rounding=ROUND_FLOOR))
        if fract_part >= 1:
            fract_part -= 1
        limit -= 1

print(mark + result)
