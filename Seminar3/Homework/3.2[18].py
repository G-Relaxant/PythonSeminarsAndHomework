"""
3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. Пользователь вводит это число с клавиатуры,
список можно считать заданным. Введенное число не обязательно содержится в списке.

Примеры/Тесты:
Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
Output: 2
Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
"""



lst1 = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8, 12, 11, 12, 12, 15, 20, 40]
x = int(input('Введите число X: '))
result = lst1[0]
diffMin = lst1[0] - x if lst1[0] > x else x - lst1[0]
diffCur = 0
diffBuf = 0
#result2 = 0

for el in lst1:
    #print(f'test el {el}')                 # test tracer
    diffCur = el - x if el > x else x - el
    #print(f'test dC {diffCur}')
    diffBuf = diffMin
    #print(f'test dB {diffBuf}')
    diffMin = diffCur if diffCur < diffMin else diffMin
    #print(f'test dM {diffMin}')
    result = el if diffCur < diffBuf else result
    #print(f'test Res {result}')
print(f"Result = {result}")

    #result2 = el if diffCur == diffBuf     # без else в однострочном виде не работает, поэтому классика ниже   \
    # if diffCur == diffBuf:                                                                                    \
    #     result2 = el                                                                                          \
    # print(f'test Res2 {result2}')                                                                             \
#                                                                                                               \
#                                                                                                               \
# if result2 < x:                                                                                               \
#     if result2 - x == diffBuf:                                                                                \
#     #print(f'test Res2Type {type(result2)}')                                                                  \
#         print(f'Results = {result} and {result2}')                                                            \ Пробовал сделать печать сразу двух чисел, если до них было одинаковое расстояние от числа Х, но чёто не работает правильно, разные косяки вылезают
#     else:                                                                                                     \
#         #print(f'test Res2Type {type(result2)}')                                                              \
#         print(f"Result = {result}")                                                                           \
# else:                                                                                                         \
#     if x - result2 == diffBuf:                                                                                \
#     #print(f'test Res2Type {type(result2)}')                                                                  \
#         print(f'Results = {result} and {result2}')                                                            \
#     else:                                                                                                     \
#         #print(f'test Res2Type {type(result2)}')                                                              \
#         print(f"Result = {result}")                                                                           \
