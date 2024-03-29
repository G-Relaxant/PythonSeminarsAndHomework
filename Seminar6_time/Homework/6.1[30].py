'''
6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
Программа принимает от пользователя три числа :

Первый элемент прогрессии, Разность (шаг) и Количество элементов
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

Напишите функцию

- Аргументы: три указанных параметра
- Возвращает: список элементов арифметической прогрессии.

Примеры/Тесты:

Ввод: 7 2 5
Вывод: [7 9 11 13 15]
Ввод: 2 3 12
Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
(*) Усложнение. Для формирования списка внутри функции используйте Comprehension

(**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input, в одну строку,
вам понадобится распаковка и Comprehension или map
'''



def inputFunc() -> tuple:
    inpStr = input('Введите числа через запятую (латинская раскладка): ')
    inpTup = tuple(inpStr.split(','))
    return inpTup

def arifProgresFunc(a: int, b: int, c: int) -> list:
    lst1 = [a]
    for idx in range(c-1):
        lst1.append(lst1[idx]+b)
    return lst1


numFirst, numStep, numCount = inputFunc()
numCount = int(numCount)
numStep = int(numStep)
numFirst = int(numFirst)
rslt = arifProgresFunc(numFirst, numStep, numCount)
print(rslt)
