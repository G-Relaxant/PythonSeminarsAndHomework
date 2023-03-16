def get_file_name() -> str:
    return input('Vvedite imya fayla: ')

def get_batch_data(name_file: str) -> list:
    lst = []
    with open('phbk.csv', 'r', encoding = 'utf-8') as file:
        for line in file:
            lst.append(list(line.split('#')))
    return lst

def record_data(name_file, data):
    with open ('phbk2.csv', 'w', encoding = 'utf-8') as file:
        for el in data:
            file.write(f'{el[0]};{el[1]};{el[2]};{el[3]}\n')

