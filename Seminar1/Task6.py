#MyVariant

# vagonPoSchetu = int(input('Введите номер вагона для посадки по счёту пассажира: '))
# vagonPoNumeracii = int(input('Введите номер посадочного вагона по нумерации: '))
# if vagonPoSchetu < vagonPoNumeracii:
#     dif = vagonPoNumeracii - 1
#     vagonsCount = dif + vagonPoSchetu
#     print(vagonsCount)
# elif vagonPoSchetu > vagonPoNumeracii:
#     dif = vagonPoSchetu - vagonPoNumeracii
#     vagonsCount = dif + vagonPoSchetu
#     print(vagonsCount)
# else:
#     print('Мало данных для вычисления правильного ответа')


#SeminarVariant

i = int(input('В какой вагон вы сели? '))
j = int(input('Какой номер этого вагона? '))
if i == j:
    print('Невозможно посчитать колво вагонов в поезде')
else:
    print(f'Колво вагонов в поезде {i + j - 1}')
