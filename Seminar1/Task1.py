#MyVariant

# n = 700
# m1 = 750
# m2 = 600
# m3 = 1400
# mCount = 3
# answer = 0
# i = 0
# mc = 0
# while i < mCount:
#     if i == 0:
#         mc = m1
#     elif i == 1:
#         mc = m2
#     else:
#         mc = m3
#     i += 1

#     if mc % n != 0:
#         answer = mc // n
#         answer += 1
#     else:
#         answer = mc / n
    
#     int(answer)             # почему то не преобразует float в int, но и ошибку не выдаёт
#     print(answer)


#SeminarVariant

n = 700
m = 1400
if m % n == 0:
    result = m // n
else:
    result = m // n + 1
print(f'Чтобы проехать {n}км машине потребуется {result}дн')
print('Чтобы проехать {0}км машине потребуется {1}дн'.format(n, result))
