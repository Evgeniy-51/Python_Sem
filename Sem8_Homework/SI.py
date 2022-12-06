import sqlite3 as sq
import datetime as dt
import view


def connection(opt, row='', row2='', row3=''):
    conn = None
    try:
        conn = sq.connect("card_file.db")
        cur = conn.cursor()

        cur.execute("""
                CREATE TABLE IF NOT EXISTS card_file(
                employer_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                surname TEXT,
                name TEXT,
                position TEXT,
                b_year TEXT,
                job_ph TEXT,
                home_ph TEXT,
                cell_ph TEXT
            )""")

        if opt == 'view_db':
            cur.execute("SELECT * FROM card_file")
            logger(opt)
            return cur.fetchall()
        elif opt == 'find_surname':
            cur.execute("SELECT * FROM card_file WHERE surname=?", (row,))
            row = cur.fetchall()
            logger([opt, row])
            return row
        elif opt == 'find_position':
            cur.execute("SELECT * FROM card_file WHERE position=?", (row,))
            row = cur.fetchall()
            logger([opt, row])
            return row
        elif opt == 'add_note':
            cur.execute("INSERT INTO card_file VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)", row)
        elif opt == 'edit_note':
            cur.execute(f"UPDATE card_file SET {row3.lower()} = '{row}'  WHERE employer_id = {row2}")
        elif opt == 'delete_note':
            cur.execute("DELETE FROM card_file WHERE employer_id=?", (row,))
        elif opt == 'if_exists':
            cur.execute("SELECT employer_id FROM card_file WHERE employer_id=?", (row,))
            return cur.fetchone()

        conn.commit()
        logger([opt, row])
        view.row_view("** Файл успешно изменен **")

    except sq.Error as e:
        if conn:
            logger('ERROR Ошибка выполнения запроса')
            view.row_view("** Ошибка выполнения запроса **")

    finally:
        if conn:
            conn.close()

def logger(data):
    curr_time = dt.datetime.now().strftime("%Y-%b-%d %H:%M")

    try:
        with open('card_file.log', 'a', encoding='utf-8') as file:
            file.write(f'{curr_time} -  {data}\n')
    except FileNotFoundError:
        print("Ошибка при работе с файлом .log")




