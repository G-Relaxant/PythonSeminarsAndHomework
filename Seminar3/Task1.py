# lst1 = str('1, 90, 2')
# print(lst1)

# print(str(90) in lst1)
# print(str(901) in lst1)

# tupl1 = 1,2,3               # КОРТЕЖ не позволяет изменять(перезаписывать элементы(ячейки))
# tupl2 = (1,2,3)             # КОРТЕЖ также можно записать в круглых скобках, разницы нет
# внутри КОРТЕЖА может быть СПИСОК, а список можно изменять(перезаписывать), но тогда это будет являться ВЛОЖЕННОЙ СТРУКТУРОЙ

# print(type(lst1))
# print(type(lst2))
# print(type(lst3))
# print(len(lst1))
# print(len(lst2))
# print(len(lst3))

# dict1 = {1:"12", "2":12221, 767:9909, example:111}     # СЛОВАРИ оформляются фигурными скобками, а содержимое ячейки представляет собой пару ключ:значение
# запрос к словарю выполняется не по индексу, а по ключу, с соблюдением типа ключа, например: print(dict1["2"]) или print(dict1[example])
# for el in dict1:
#     print(el)

# lst1 = [1,4,6,8,9,12]       # СПИСОК мутабельный(можно изменять(перезаписывать ячейки))
# СПИСОК в питоне реализован как Массив Ссылок, то есть МАССИВ на языке C

# for el in lst1:
#     print(el)

# for i in range(len(lst1)):
#     print(i, lst1[i])
