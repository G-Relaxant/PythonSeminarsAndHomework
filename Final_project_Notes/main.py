import ex_imp as exp
import func as fc

notes = []

def menu(data: list):
    print()
    print('БЛОКНОТсЗаМеТкАмИ-NOTES')
    while True:
        print()
        print('Выберите действие:')
        print('1 - Выйти из блокнота')
        print('2 - Создать новую заметку')
        print('3 - Распечатать весь блокнот')
        print('4 - Выбрать заметку по началу названия')
        print('5 - Изменить существующую заметку')
        print('6 - Удалить заметки')
        print('7 - Импортировать заметки из файла')
        print('8 - Экспортировать заметки в файл')
        print()
        get = input('Введите действие: ')
        if get == '1':
            get = input('Если вы не экспортируете заметки, то они не сохранятся. Закрыть блокнот? (y/n): ')
            if get == 'y' or get == 'yes':
                print('Вы вышли из блокнота. Если вы не экспортировали заметки, то они не сохранились')
                break
            else:
                continue
        elif get == '2':
            data = fc.create(data,fc.get_data())
        elif get == '3':
            fc.print_all(data)
        elif get == '4':
            fc.select(data)
        elif get == '5':
            fc.update(data)
        elif get == '6':
            fc.delete(data)
        elif get == '7':
            name_file = exp.get_file_name()
            pull = exp.import_file(name_file)
            data =fc.pull_create(data, pull)
        elif get == '8':
            name_file = exp.get_file_name()
            exp.export_file(name_file, data)
        else:
            print('Некорректный ввод')

menu(notes)
