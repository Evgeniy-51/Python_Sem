#  Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('polinom.txt') as file1:
    exp1 = ['0'] + file1.readline().split()
with open('polinom2.txt') as file2:
    exp2 = ['0'] + file2.readline().split()

dict1, dict2 = {}, {}
max_key = 0
res = ''


def list_modify(lst, dict):
    global max_key
    for i in range(1, len(lst) - 1, 2):
        xx = lst[i].find('x^')
        if xx != -1:
            val = -int(lst[i][:xx]) if lst[i - 1] == '-' else int(lst[i][:xx])
            key = lst[i][xx + 2:]
            dict[key] = val
            if int(key) > max_key:
                max_key = int(key)
        elif lst[i].find('x') != -1:
            x = lst[i].find('x')
            val = -int(lst[i][:x]) if lst[i - 1] == '-' else int(lst[i][:x])
            dict['1'] = val
        else:
            val = -int(lst[i]) if lst[i - 1] == '-' else int(lst[i])
            dict['0'] = val


list_modify(exp1, dict1)
list_modify(exp2, dict2)


def incut(i):
    if i > 1:
        return f"x^{i}"
    elif i == 1:
        return f"x{i}"
    else:
        return ''


for i in range(max_key, -1, -1):
    k = str(i)
    if k in dict1 and k in dict2:
        sum = dict1[k] + dict2[k]
        res += f" + {sum}{incut(i)}" if sum > 0 \
            else f" - {abs(sum)}{incut(i)}"
    elif k in dict1:
        res += f" + {dict1[k]}{incut(i)}" if dict1[k] > 0 \
            else f" {abs(dict1[k])}{incut(i)}"
    elif k in dict2:
        res += f" + {dict2[k]}{incut(i)}" if dict2[k] > 0 \
            else f" - {abs(dict2[k])}{incut(i)}"
res += ' = 0'
if res[:3] == ' + ':
    res = res[3:]
else:
    res = '-' + res[3:]


print(*exp1[1:])
print(*exp2[1:])
print(res)
