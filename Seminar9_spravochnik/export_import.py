def get_file_name() -> str:
    return input('Vvedite imya fayla: ')

def get_batch_data(name_file: str) -> list:
    lst = []
    with open(name_file, 'r', encoding = 'utf-8') as file:
        for line in file:
            line.strip()    # strip не срабатывает, пробелы остаются(если добавить в л17)
            lst.append(list(line.strip().split(';')))   # strip не срабатывает, пробелы остаются(если добавить в л17)
    return lst

def record_data(name_file, data):
    with open (name_file, 'w', encoding = 'utf-8') as file:
        for el in data:
            # file.write(f'{el[0]};{el[1]};{el[2]};{el[3]}\n')
            # file.write(f'{el[4]};{el[5]}\n')
            file.write(f'{el[0]};{el[1]};{el[2]};{el[3]};{el[4]};{el[5]}\n')
