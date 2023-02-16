'''
Напишите программу для печати всех уникальных значений в списке словарей.

Примечание: Список словарей задан изначально. Пользователь его не вводит

Обратите внимание, что в словарях может быть один или несколько элементов

Примеры/Тесты:

Input: [{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005", "XI": "D011"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 ", "XII": "D001"}]

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

[*] Усложнение. Проверку уникальности строк сделайте без учета пробелов до и после значимой части строки

[**] Усложнение. Запишите алгоритм в одну строку, используйте Comprehension
'''



dict_list = [{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005", "XI": "D011"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ":" S007 ", "XII": "D001"}]

# for i in range(len(dict_list)):   # 1 вариант перебора циклом
#     for j in dict_list[i]:
#         print(j)

# for el in dict_list:                # 2 вариант
#     for j in el:
#         print(j)         # печать ключа
#         print(el[j])     # печать значения(содержимого) ключа

# for el in dict_list:                # 3 вариант (более предпочтительный, так как задействуем методы и сокращаем код)
#     for value in el.values():       # метод .values
#         print(value)

set_1 = set()                       # метод set()
for el in dict_list:                                    # 4 вариант (более предпочтительный для питона)
    for value in el.values():       # метод .values
        set_1.add(value.strip())    # метод .add и .strip   Strip убирает ненужные(незначимые) элементы из текста, например пробелы и табуляцию
print(set_1)