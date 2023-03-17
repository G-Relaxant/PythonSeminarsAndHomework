def create(data: list, el: list) -> list:
    data.append(el)
    return data

def batch_create(data: list, batch_data) -> list:
    for el in batch_data:
        data = create(data, el)
    return data

def print_phone_book(data: list) -> None:
    #print(f'Kontakti: {data}')
    for el in data:
        print_record(el)
    
def print_record(record: list) -> None:
    print(f'{record[0]}, {record[1]}, {record[2]}, {record[3]}')

def get_data() -> list:
    print()
    surname = input('Vvedite familiyu: ')
    name = input('Vvedite imya: ')
    phone = input('Vvedite nomer telefona: ')
    discription = input('Vvedite opisanie: ')
    return [surname, name, phone, discription]

def read(data: list) -> list:
    part_surname = input('Vvedite pervie bukvi familii: ')
    for el in data:
        if part_surname.casefold() in (el[0]).casefold():
            return el

def update(data: list) -> list:
    change_contact = read(data)
    while True:
        print(f'Vi vibrali: {change_contact}')
        print()
        print('Viberite deystvie: ')
        print('1 - Viyti v glavnoe menu')
        print('2 - Izmenit familiyu')
        print('3 - Izmenit imya')
        print('4 - Izmenit nomer telefona')
        print('5 - Izmenit opisanie')
        print()
        for el in data:
            if el == change_contact:
                get_action = input('Vvedite deystvie: ')
                if get_action == '1':
                    print('Perehod v glavnoe menu')
                    break
                elif get_action == '2':
                    change_contact[0] = input('Vvedite familiyu: ')
                elif get_action == '3':
                    change_contact[1] = input('Vvedite imya: ')
                elif get_action == '4':
                    change_contact[2] = input('Vvedite telefon: ')
                elif get_action == '5':
                    change_contact[3] = input('Vvedite opisanie: ')
                else:
                    print('Nekorrektniy vvod')
                el = change_contact
        return data

def delete(data: list) -> list:
    del_contact = read(data)
    print(f'Vi udalili: {del_contact}')
    for el in data:
        if el == del_contact:
            data.remove(el)
            break
    return data
