"""
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

Примечание: Пользователь может вводить значения списка или список задан изначально.

Примеры/Тесты:

Input: [1, 2, 3, 4, 5] k = 3

Output: [4, 5, 1, 2, 3]
"""


# k = int(input('Введите положительное число: '))
k = 4
list_1 = [1, 2, 3, 4, 5]
list_2 = []

for i in range(k, len(list_1)):
    list_2.append(list_1[i])

for i in range(k):
    list_2.append(list_1[i])
print(list_2)
