def inp_data(ID) -> dict:
    person = {}
    person["id"] = ID
    person["first_name"] = input("Введите ИМЯ: ")
    person["last_name"] = input("Введите ФАМИЛИЮ: ")
    person["bdate"] = input("Введите ДАТУ РОЖДЕНИЯ: ")
    person["job_place"] = input("Введите МЕСТО РАБОТЫ: ")

    tel = []
    val = True
    while val:
        val = input("Введите НОМЕРА ТЕЛЕФОНА или <Enter> для прекращения ввода: ")
        if len(val) > 5: tel.append(val)

    person["tel"] = tel

    return person


def menu() -> str:
    while True:
        print("\n[MENU]  Выберите действие:")
        print("  <1> -  добавить запись")
        print("  <2> - посмотреть все записи")
        print("<Enter> - выйти из программы")
        val = input()
        if val in ('1', '2'):
            return val
        else:
            exit()
