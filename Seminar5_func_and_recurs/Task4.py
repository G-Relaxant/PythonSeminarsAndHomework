"""
Напишите функцию, которая принимает число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Если число простое - функция возвращает True, если нет - возвращает False
Примеры/Тесты:
<function_name>(13) -> True
<function_name>(10) -> False
"""


#MyVariant
# def is_primeNumber(n: int) -> bool:   #type hinting annotation
#     rslt = True
#     for idx in range(2, n): #TypeError: 'str' object cannot be interpreted as an integer
#         if n % idx != 0:    #TypeError: not all arguments converted during string formatting
#             continue
#         else:
#             rslt = False
#             break
#     return rslt

# num = input('Введите число: ')
# print(is_primeNumber(num))



#SeminarVariant
def is_prime_number(n: int) -> bool:    #type hinting annotation
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime_number(13))
