'''
№7.1[###]. Дан текстовый csv файл. Разделитель данных #.

Каждая строка файла представляет собой запись вида ФИО

Например:

Иванов#Иван#Иванович

Петров#Петр#Петрович

Соколов#Илья#Григорьевич

1) Необходимо вывести эти данные на экран построчно в виде:

Иванов Иван Иванович

Петров Петр Петрович

2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]

[*] Усложнение. Файл находится в поддиретории data текущей директории. Сформировать путь к нему с использованием

os.path и pathlib

№7.2[###]. Продолжение предыдущей задачи

Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]

необходимо преобразовать к виду:

Иванов И.И.

Петров П.П.

Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.

[*] Усложнение. Данные необходимо записать в два разных файла:

В первый - в виде Иванов И.И.

Во второй - в виде Иванов-И-И

[*****] Усложнение. Вам известно, что (в перспективе) подобных спецификаций может быть много. Не две, а пять или десять

Как улучшить свой код в этом случае, сделать его легко расширяемым?
'''




from pathlib import Path            #\
MAIN_DIR = Path(__file__).parent    # | задаём главную(корневую) папку для пути обращения(поиска) к файлу

with open(MAIN_DIR / 'data_dir' / 'data3.txt', mode = 'r', encoding = 'utf-8') as fileRead:         # блок WITH OPEN наиболее предпочтителен при работе с файлами
    result = []
    for line in fileRead:
        tmp = line.strip().split('#')
        result.append(tmp)
        print(*tmp)
print('*'*20)
for word1, word2, word3, word4 in result:
    print(f'{word1} {word2[0]}.{word3[0]}. {word4}')


with open(MAIN_DIR / 'data_dir' / 'rezults' / 'result1.txt', mode = 'w', encoding = 'utf-8') as fileWrite:  # создаём новый файл
    for word1, word2, word3, word4 in result:
        template1 = f'|||{word4}  {word1} {word2[0]}.{word3[0]}.'
        fileWrite.write(template1)

with open(MAIN_DIR / 'data_dir' / 'rezults' / 'result2.txt', mode = 'w', encoding = 'utf-8') as fileWrite:  # создаём новый файл
    for word1, word2, word3, word4 in result:
        template1 = f'|||{word4}  {word1} {word2[0]}.{word3[0]}.\n'     # \n - специальный символ, который задаёт переход на следующую строку текст. редактору
        fileWrite.write(template1)



with open(MAIN_DIR / 'data_dir' / 'rezults' / 'result3.txt', mode = 'w', encoding = 'utf-8') as fileWrite1:     # создаём новые файлы за один блок (с вложенным блоком для 2го файла)
    with open(MAIN_DIR / 'data_dir' / 'rezults' / 'result4.txt', mode = 'w', encoding = 'utf-8') as fileWrite2:
        for word1, word2, word3, word4 in result:
            template1 = f'|||{word4}  {word1} {word2[0]}.{word3[0]}.'
            template2 = f'|||{word4}  {word1} {word2[0]}.{word3[0]}.\n'
            fileWrite1.write(template1)
            fileWrite2.write(template2)
