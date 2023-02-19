"""
Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

*Пример:*

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1
"""



lst1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find_str = "qwe"
counter = 0
conditPoint = 2

for idx, value in enumerate(lst1):
    print(f'test Cou {counter}, idx {idx}, value {value}')
    if value == find_str:
        print(f'test 1if')
        counter +=1
    if counter == conditPoint:
        print(f'Result: {idx}')
        break
if counter != conditPoint:
    print('-1')
