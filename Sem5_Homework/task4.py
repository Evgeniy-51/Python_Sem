# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Входные данные в файле _data_file.txt. Запакованные помещаются в _packed.txt,
# откуда распаковываются и сохраняются в unpacked.txt

try:
    with open('_data_file.txt') as data:
        text = data.readlines()
except FileNotFoundError:
    print("Ошибка при работе с файлом")


def pack(line):
    line = line + ' '
    res = ''
    while len(line) > 1:
        if line[0] == line[1]:
            i = 0
            while i < 12 and line[i] == line[i + 1] and len(line) > 1:
                i += 1
            res += f"#{i - 3}{line[i]}" if i > 2 else (i + 1) * line[i]
            line = line[(i + 1):]
        else:
            res += line[0]
            line = line[1:]
    return res


def unpack():
    try:
        with open('_packed.txt') as packed_txt:
            packed = packed_txt.readlines()
    except FileNotFoundError:
        print("Ошибка при работе с файлом")

    unpack = open('_unpacked.txt', 'w')
    for line in packed:
        res_line = ''
        k = 0
        while k < len(line) - 1:
            if line[k] == '#' and str(line[k + 1]).isdigit():
                res_line += line[k + 2] * (int(line[k + 1]) + 4)
                k += 3
            else:
                res_line += line[k]
                k += 1

        unpack.write(res_line + '\n')
        print(res_line)

    pack_file.close()


pack_file = open('_packed.txt', 'w')
for line in text:
    pack_file.write(pack(line))
pack_file.close()

unpack()
