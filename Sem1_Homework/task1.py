# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

num = int(input("Enter a number from 1 to 7 (day of the week): "))

if num < 1 or num > 7:
    print("Really??")
else:
    print("No" if num < 6 else "Yes, it's a weekend!")
