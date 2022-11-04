# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random
from time import sleep


def bot_first(amount):
    print("Я беру 20.")
    amount -= 20
    while amount > 0:
        print(f'Всего конфет: {amount}. Сколько возьмете?')
        move = check_move(amount)
        amount -= move
        if amount <= 0:
            print('OK, ты выиграл!')
        else:
            bot_move = 29 - move
            print(f'Теперь конфет: {amount}. Я беру {bot_move}')
            amount -= bot_move
            if amount == 0:
                print('Я выиграл!')
                break


def bot_second(amount):
    def answer(amount, move):
        if amount > 107:
            return 28
        elif amount > 87:
            return 29 - move
        elif amount == 58 or amount == 29:
            return 1
        elif 58 < amount <= 87:
            res = amount - 58
            return res if res < 28 else 28
        elif 28 < amount < 58:
            res = amount - 29
            return res if 0 < res < 28 else 28
        else:
            return amount

    while amount > 0:
        print(f'Всего конфет: {amount}. Сколько возьмете?')
        move = check_move(amount)
        amount -= move
        if amount <= 0:
            print('OK, Вы выиграли!')
        else:
            bot_move = answer(amount, move)
            print(f'Теперь конфет: {amount}. Я беру {bot_move}')
            amount -= bot_move
            if amount == 0:
                print('Я выиграл!')
                break


def two_gamers(amount):
    gamer1 = input("Первый игрок, введите свое имя:  ")
    gamer2 = input("Второй игрок, введите свое имя:  ")
    print("Идет жеребьевка...")
    for i in range(10):
        print('-', sep=' ', end=' ', flush=True)
        sleep(0.3)

    dice = random.randint(1, 2)
    if dice == 2:
        gamer1, gamer2 = gamer2, gamer1
    turn = 1

    print(f"\nИгрок {gamer1} ходит первым")
    while amount > 0:
        gamer = gamer1 if turn > 0 else gamer2
        print(f'Всего конфет: {amount}. {gamer}, cколько возьмете?')
        move = check_move(amount)
        amount -= move
        if amount <= 0:
            print(f"{gamer} выиграл!")
        turn = -turn


def check_move(amount):
    while True:
        val = input()
        if val.isdigit():
            val = int(val)
            if 0 < val < 29:
                if val < amount:
                    return val
                else:
                    print(f"Осталось только {amount}, и Вы их забрали!")
                    return amount
            else:
                print("Можно взять не более 28 и не менее 1!")
        else:
            print("Вводите только числа!")


def choice():
    while True:
        val = input()
        if val == '1' or val == '2':
            return val
        else:
            print("Допустимые значения: 1 или 2. Сделайте свой выбор:")


# amount = 107
amount = 2021
print("\nУсловия игры: на столе 2021 конфета. Можно взять от 1 до 28. Кто взял последнюю, тому достаются все.")
print("Хотите играть против алгоритма или с другим игроком?")
print("[1] - против алгоритма  \n[2] - с другим человеком")
variant = choice()
if variant == '1':
    print("Хотите ходить первым [1]  или вторым [2]?")
    first_move = choice()
    if first_move == '1':
        bot_second(amount)
    else:
        bot_first(amount)
else:
    two_gamers(amount)
