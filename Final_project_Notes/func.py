import datetime

def create(data: list, el: list) -> list:
    data.append(el)
    return data

def pull_create(data: list, pull) -> list:
    for el in pull:
        data = create(data, el)
    return data

def print_all(data: list) -> None:
    print()
    for el in data:
        print_note(el)
    
def print_note(record: list) -> None:
    print(f'{record[0]}, {record[1]}')
    print(f'{record[2]}, {record[3]}')
    print()

def get_data() -> list:
    print()
    name = input('Введите название заметки: ')
    text = input('Введите текст заметки: ')
    date_time = datetime.datetime.today().strftime("Дата создания: %d-%m-%y Время: %H.%M.%S")
    dtc = "Не изменялась"
    return [name, text, date_time, dtc]

def read(data: list) -> list:
    part_note = input('Введите первые буквы названия заметки: ')
    for el in data:
        if part_note.casefold() in (el[0]).casefold():
            return el

def update(data: list) -> list:
    sel_note = read(data)
    while True:
        print(f'Вы выбрали: {sel_note}')
        print()
        print('Выберите действие: ')
        print('1 - Выйти в главное меню')
        print('2 - Изменить название заметки')
        print('3 - Изменить текст заметки')
        print()
        for el in data:
            if el == sel_note:
                get_action = input('Введите действие: ')
                if get_action == '1':
                    print('Вы вышли в главное меню')
                    break
                elif get_action == '2':
                    sel_note[0] = input('Введите название заметки: ')
                elif get_action == '3':
                    sel_note[1] = input('Введите основной текст заметки: ')
                else:
                    print('Некорректный ввод')
                el = sel_note
        sel_note[3] = datetime.datetime.today().strftime("Дата изменения: %d-%m-%y Время: %H.%M.%S")
        return data

def delete(data: list) -> list:
    del_note = read(data)
    print(f'Вы удалили: {del_note}')
    for el in data:
        if el == del_note:
            data.remove(el)
            break
    return data

def select(data: list) -> None:
    sel_note = read(data)
    print(f'Вы выбрали: {sel_note}')
