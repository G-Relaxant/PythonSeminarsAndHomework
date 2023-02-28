'''
Два различных натуральных числа n и m называются дружественными,
если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
Например, 220 и 284 – дружественные числа.
220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, — их сумма равна 284.
284: 1, 2, 4, 71 и 142, — их сумма равна 220.
Первые пары дружественных чисел:
220, 284; 1184, 1210; 2620, 2924; 5020, 5564; 6232, 6368

Для заданного числа number выведите все пары дружественных чисел, каждое из которых не превосходит number.
Напишите функцию:
Аргументы: целое число
Печатает все пары дружественных чисел, не превосходящих аргумент.
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

Примечание:
1. Выделите значимые куски алгоритма и оформите их в виде функций
2. Задокументируйте созданные функции
3. Используйте type hinting

Примеры/Тесты:
<function_name>(300)
220 284
<function_name>(10000)
220 284
1184 1210
2620 2924
5020 5564
'''



#Variant 1
# def isFriendNumber(a: int, b: int) -> bool:
#     sumA = 0
#     for idx in range(1, a):
#         if a % idx == 0:
#             sumA += idx
#     sumB = 0
#     for idx in range(1, b):
#         if b % idx == 0:
#             sumB += idx
#     if sumA == b and sumB == a and a != b:
#         return True
#     else:
#         return False

# def paraNumbers(n: int) -> None:
#     for idx in range(1, n):
#         for idx2 in range(1, n):
#             if idx < idx2:
#                 if isFriendNumber(idx, idx2):
#                     print(idx, idx2)

# numb = 1300

# paraNumbers(numb)


#Variant 2
def paraNumbers(n: int) -> None:
    for idx in range(1, n):
        sum1 = sumDivisor(idx)
        sum2 = sumDivisor(sum1)
        if idx == sum2 and idx < sum1:
            print(idx, sum1)

def sumDivisor(a: int) -> int:
    '''
    return sum of divisor for number a
    :param a: int. number for ... calculate sum
    :return: int. sum of divisor
    '''
    sumA = 0
    for idx in range(1, a):
        if a % idx == 0:
            sumA += idx
    return sumA

numb = 11111

paraNumbers(numb)