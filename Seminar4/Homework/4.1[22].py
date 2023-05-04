"""
4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное диагностическое сообщение

Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

Примеры/Тесты:
Input1: 2 4 6 8 10 12 10 8 6 4 2
Input2: 3 6 9 12 15 18
Output: 6 12     Обратите внимание: Без скобочек, в одну строку

Input1: 2 4 6 8 10 10 8 6 4 2
Input2: 3 9 12 15 18
Output: Повторяющихся чисел нет
"""




tup1 = 4, 8, 9, 4, 1, 2, 5, 5, 11, 12, 7, 3, 4
tup2 = 9, 13, 6, 4, 2, 8, 7, 11, 11
listRslt = []

for idx in range(len(tup1)):
    if tup1[idx] in listRslt:
        continue
    else:
        for idx2 in range(len(tup2)):
            if tup1[idx] == tup2[idx2]:
                listRslt.append(tup1[idx])
                break

if listRslt != []:
    #print('test1')
    #print(f'test {listRslt}')
    strRslt = ''
    #listRslt = listRslt.sort()     # почему то не работает, хотя должен работать со списками
    listRslt = sorted(listRslt)     # Функция сортировки. Метод .sort() почему то не работает, хотя должен работать со списками
    for idx in range(len(listRslt)):
        #print('test2')
        strRslt += f'{listRslt[idx]} '
    print(strRslt[:-1])
else:
    print('Повторяющихся чисел нет')
