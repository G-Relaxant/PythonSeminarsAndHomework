"""
5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения.
Циклы использовать нельзя

Примеры/Тесты:
<function_name>(2,0) -> 1
<function_name>(2,1) -> 2
<function_name>(2,3) -> 8
<function_name>(2,4) -> 16
"""

def funcExponentiation(a: int, b: int) -> int:
    c = a
    if b != 2:
        b = b - 1
        c = funcExponentiation(a, b)
    c = c*a
    return c

numA = int(input('Input A: '))
numB = int(input('Input B: '))

if numB == 0:
    print(f'Result = 1')
elif numB == 1:
    print(f'Result = {numA}')
else:
    rslt = funcExponentiation(numA, numB)
    print(f'Result = {rslt}')
