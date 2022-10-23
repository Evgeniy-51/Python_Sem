#  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("\nВведите число: "))
res_list = []

i = 2
while i <= num:
    if not num % i:
        res_list.append(i)
        num /= i
    else:
        i += 1

print(res_list)
