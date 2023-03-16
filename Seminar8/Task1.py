'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
'''


#ДЛЯ КОРРЕКТНОЙ РАБОТЫ ПРОГИ, ПАПКА СЕМИНАР-8 ДОЛЖНА БЫТЬ КОРНЕВОЙ (В VSCODE НУЖНО ОТКРЫТЬ ТОЛЬКО ЭТУ ПАПКУ)

# phoneBook = {1:('Nehaev', 'Mihail', '8900111', 'friend'),
#         2:('Petrov', 'Sergey', '8901222', 'enemy')}
phoneBook = {}
idClient = 0

def menu(data: dict, idClient: int):
    while True:
        print('Viberite deystvie: ')
        print('1 - sozdat novuyu zapis')
        print('2 - raspechatat soderzhimoe spravochnika')
        print('3 - importirovat dannie iz text fayla')
        print('4 - exportirovat dannie v text fayl')
        get = input('Vvedite deystvie: ')
        if get == '':
            print('Ne vibrano deystvie')
            break
        elif get == '1':
            idClient += 1
            data = create(data, idClient, getDataInput())
        elif get == '2':
            printPhBk(data)
        elif get == '3':
            nameFile = getFileName()
            batchData = getBatchData(nameFile) 
            data = batchCreate(data, batchData, idClient)
        elif get == '4':
            nameFile = getFileName()
            giveBatchData(data, nameFile)
        else:
            print('ShinimaHuynya')

def create(data: dict, id: int, elem: tuple) -> dict:
    data[id] = elem
    return data

def printPhBk(data: dict) -> None:
    for key, values in data.items():
        print(f'id: {key}, {values}')

def getDataInput() -> tuple:
    surname = input('Vvedite familiyu: ')
    name = input('Vvedite imya: ')
    phone = input('Vvedite nomer telefona: ')
    discription = input('Vvedite opisanie: ')
    return (surname, name, phone, discription)

def getFileName() -> str:
    return input('Vvedite imya fayla: ')

def getBatchData(nameFile: str) -> list:
    lst = []
    with open(nameFile, 'r', encoding = 'utf-8') as file:         # читаем файл
        for line in file:
            temp = tuple(line.split('#'))
            lst.append(temp)
    return lst

def giveBatchData(data: dict, nameFile: str) -> None:
    with open(nameFile, mode = 'w', encoding = 'utf-8') as file:  # создаём новый файл
        for key, values in data.items():
            temp = f'id: {key}, {values}\n'     # \n - специальный символ, который задаёт переход на следующую строку текст. редактору
            file.write(temp)

def batchCreate(data: dict, batchData, idClient) -> dict:
    for elem in batchData:
        data = create(data, idClient, elem)
        idClient += 1
    return data

menu(phoneBook, idClient)

#ДЛЯ КОРРЕКТНОЙ РАБОТЫ ПРОГИ, ПАПКА СЕМИНАР-8 ДОЛЖНА БЫТЬ КОРНЕВОЙ (В VSCODE НУЖНО ОТКРЫТЬ ТОЛЬКО ЭТУ ПАПКУ)
