# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

answer = ("X > 0, Y > 0",
          "X < 0, Y > 0",
          "X < 0, Y < 0",
          "X > 0, Y < 0")
quarter = 0

while not quarter:
    quarter = int(input("Введите № четверти:  "))
    if quarter < 1 or quarter > 4:
        print("Их всего четыре...")
        quarter = 0

print(answer[quarter - 1])
