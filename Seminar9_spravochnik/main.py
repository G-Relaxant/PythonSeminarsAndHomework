import export_import as ex
import model as m

phone_book = []

def menu(data: list):
    while True:
        print()
        print('Viberite deystvie:')
        print('1 - Viyti iz spravochnika')
        print('2 - Sozdat novuyu zapis')
        print('3 - Raspechatat soderzhimoe spravochnika')
        print('4 - Vibrat zapis po 1oy chasti familii')
        print('5 - Izmenit pole(ya) vibrannoy zapisi')
        print('6 - Udalit zapisi iz spravochnika')
        print('7 - Importirovat dannie iz text fayla')
        print('8 - Exportirovat dannie v text fayl')
        print()
        get = input('Vvedite deystvie: ')
        if get == '1':
            print('Do svidaniya')
            break
        elif get == '2':
            data = m.create(data, m.get_data())
        elif get == '3':
            m.print_phone_book(data)
        elif get == '4':
            m.select_contact(data)
        elif get == '5':
            m.update(data)
        elif get == '6':
            m.delete(data)
        elif get == '7':
            name_file = ex.get_file_name()
            batch_data = ex.get_batch_data(name_file)
            data = m.batch_create(data, batch_data)
        elif get == '8':
            name_file = ex.get_file_name()
            ex.record_data(name_file, data)
        else:
            print('Nekorrektniy vvod')


menu(phone_book)
