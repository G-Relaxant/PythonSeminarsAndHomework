'''
5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических
операций допускаются только +1 и -1. Циклы использовать нельзя

Примеры/Тесты:
<function_name>(0,0) -> 0
<function_name>(0,2) -> 2
<function_name>(3,0) -> 3
'''



def funcSum(a: int, b: int) -> int:
    c = a
    if b != 0:
        b = b - 1
        c = funcSum(a, b) + 1
    return c

numA = int(input('Input A: '))
numB = int(input('Input B: '))

if numA < 0 or numB < 0:
    print('Repeat input with positive numbers')
elif numA >= numB:
    rslt = funcSum(numA, numB)
    print(f'Result = {rslt}')
else:
    rslt = funcSum(numB, numA)
    print(f'Result = {rslt}')
