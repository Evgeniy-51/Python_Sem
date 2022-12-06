import UI
import SI
import view


def run():
    while True:
        option = UI.menu()

        if option == '1':  # view all
            table = SI.connection('view_db')
            view.table_view(table)

        elif option == '2':  # find by surname
            desired = UI.get_value('ФАМИЛИЮ')
            table = SI.connection('find_surname', desired)
            if table:
                view.table_view(table)
            else:
                view.row_view("Такая запись не найдена...")

        elif option == '3':  # find by position
            desired = UI.get_value('ДОЛЖНОСТЬ')
            table = SI.connection('find_position', desired)
            if table:
                view.table_view(table)
            else:
                view.row_view("Такая запись не найдена...")

        elif option == '4':  # add
            row = UI.add_row()
            SI.connection('add_note', row)

        elif option == '5':  # edit
            edit_row = UI.get_value('ID записи, которую требуется изменить')
            if_exists = SI.connection('if_exists', edit_row)
            if if_exists:
                edit_field = UI.choose_field().lower()
                if edit_field:
                    desired = UI.get_value(f'{edit_field}')
                    SI.connection('edit_note', desired, edit_row, edit_field)
                else:
                    continue
            else:
                view.row_view("Нет такого ID")

        elif option == '6':  # delete
            desired = UI.get_value('ID удаляемой строки')
            if_exists = SI.connection('if_exists', desired)
            if if_exists:
                SI.connection('delete_note', desired)
            else:
                view.row_view("Нет такого ID")

        input("Нажмите <Enter> для продолжения ...")


