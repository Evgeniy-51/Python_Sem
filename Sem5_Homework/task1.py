# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв"

text = 'Буква  забава буЛавка Вакса бумага - абзаЦ'


def check(elem):
    elem = elem.lower()
    return False if 'а' in elem and 'б' in elem and 'в' in elem else True


text = ' '.join(filter(check, text.split()))
print(text)
