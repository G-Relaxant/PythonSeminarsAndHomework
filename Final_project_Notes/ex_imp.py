def get_file_name() -> str:
    return input('Введите полное имя файла(вместе с расширением): ')

def import_file(name_file: str) -> list:
    lst = []
    with open(name_file, 'r', encoding = 'utf-8') as file:
        for line in file:
            line.strip()
            lst.append(list(line.strip().split(';')))
    return lst

def export_file(name_file, data):
    with open (name_file, 'w', encoding = 'utf-8') as file:
        for el in data:
            file.write(f'{el[0]};{el[1]};{el[2]};{el[3]}\n')
