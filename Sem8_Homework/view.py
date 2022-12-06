from prettytable import PrettyTable as pt


def table_view(data: list):
    table = pt()
    table.field_names = ['ID', 'ФАМИЛИЯ', 'ИМЯ', 'ДОЛЖНОСТЬ', 'ГОД РОЖДЕНИЯ', 'РАБ.ТЕЛЕФОН', 'ДОМ.ТЕЛЕФОН',
                          'МОБ.ТЕЛЕФОН']
    table.add_rows(data)
    print(table)


def row_view(data: str):
    print(data)


