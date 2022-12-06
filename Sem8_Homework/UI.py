import sys
import view


def add_row() -> list:
    res = []
    titles = ['ФАМИЛИЮ', 'ИМЯ', 'ДОЛЖНОСТЬ', 'ГОД РОЖДЕНИЯ', 'РАБ. ТЕЛЕФОН', 'ДОМ. ТЕЛЕФОН', 'МОБ. ТЕЛЕФОН']
    for pos in titles:
        val = input(f'Введите {pos}:   ').strip().title()
        val = val if val else 'нет данных'
        res.append(val)

    return res


def get_value(data: str) -> str:
    return input(f'Введите {data}: ').strip().title()


def menu() -> str:
    while True:
        view.row_view("""\n
        [MENU]  Выберите действие:
        <1> - посмотреть все записи
        <2> - найти запись по фамилии
        <3> - найти запись по должности
        <4> -  добавить запись
        <5> -  редактировать запись
        <6> -  удалить запись
        ------------------------------------
        <q> или <Enter> - выйти из программы
        """)

        val = input('\t\t')
        if val in ('1', '2', '3', '4', '5', '6'):
            return val
        elif val in ('', 'q'):
            sys.exit()


def choose_field() -> str:
    while True:
        view.row_view("""\n
        КАКОЕ ПОЛЕ ТРЕБУЕТСЯ ИЗМЕНИТЬ?
        <1> - Фамилия
        <2> - Имя
        <3> - Должность
        <4> - Год рождения
        <5> - Телефон рабочий
        <6> - Телефон домашний
        <7> - Телефон мобильный
        -------------------------------------
        <q> или <Enter> - отмена
        """)

        val = input('\t\t')
        if val == '1':
            return 'surname'
        elif val == '2':
            return 'name'
        elif val == '3':
            return 'position'
        elif val == '4':
            return 'b_year'
        elif val == '5':
            return 'job_ph'
        elif val == '6':
            return 'home_ph'
        elif val == '':
            return 'cell_ph'
        elif val in ('', 'q'):
            return None
        else:
            view.row_view("Нет такого пункта, введите снова")
