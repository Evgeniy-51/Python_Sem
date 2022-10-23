# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input("\nВведите натуральную степень k: "))
res = []
check_sum = 0
def rnd(): return random.randint(0, 100)


for i in range(k, 1, -1):
    c = rnd()
    if c:
        check_sum += 1
        res.append(f"x^{i}" if c == 1 else f"{c}x^{i}")

c = rnd()
if c:
    check_sum += 1
    res.append('x' if c == 1 else f"{c}x")

c = rnd()
if c:
    res.append(f"{c}")

res_line = "Все коофициенты равны нулю :(" if not check_sum \
    else ' + '.join(res) + ' = 0'

with open('polinom.txt', 'a') as file:
    file.write(res_line + '\n')

print(res_line)
