import json
import UI
import view


def read_file():
    try:
        with open('tel_book.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        print('Ошибка при работе с файлом')


def write_file(data):
    try:
        with open('tel_book.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
            print("Запись успешно добавлена!")
    except:
        print('Ошибка при работе с файлом')


def max_id():
    arr = []
    for i in j_data["response"]:
        arr.append(i["id"])
    return max(arr)


def run():
    global j_data
    j_data = read_file()
    operation = UI.menu()

    if operation == '1':
        curr_id = max_id() + 1
        curr_data = UI.inp_data(curr_id)
        j_data["response"].append(curr_data)
        write_file(j_data)

    elif operation == '2':
        for item in j_data["response"]:
            view.consol_out(item)
