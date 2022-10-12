# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

s = range(2)
res = True

for x in s:
    for y in s:
        for z in s:
            if not (not (x or y or z) == (not x and not y and not z)):
                res = False
                break

print(res)
