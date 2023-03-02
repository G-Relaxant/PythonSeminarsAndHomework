lst1 = [['Кокос', 'Мандарин', 'Горох'],
        ['Кокосик', 'Мандаринчик', 'Горошек'],
        ['Клубника', 'Малинка', 'Ягодка'],]

def template1(word1, word2, word3):
    return f'{word1}-{word2[0]}-{word3[0]}'

lst2 = [f'{obj[0]}-{obj[1][0]}-{obj[2][0]}' for obj in lst1]
lst3 = [f'{word1}-{word2[0]}-{word3[0]}' for word1, word2, word3 in lst1]
lst4 = [template1(word1, word2, word3) for word1, word2, word3 in lst1]

lst5 = [(lambda x,y,z: f'{x}-{y[0]}-{z[0]}')(x,y,z) for x, y, z in lst1] # запись comprehension с лямбда функцией

#lambda x,y,z: f'{x}-{y[0]}-{z[0]}'  # "лямбда функция"   одноразовая функция

print(lst1)
print()
print(lst2, lst3, lst4, lst5)

print()

def template2(obj):
    word1, word2, word3 = obj
    return f'{word1}-{word2[0]}-{word3[0]}'

lst6 = list(map(template2, lst1))   # функция "map" и пример вложенной функции(функ template2 вложена в функ map), влож.функ. также называются функциями высшего порядка
print(lst6)

print()

def filter1(obj):
    word1, word2, word3 = obj
    if word1[0] == 'К': return True
    return False

lst7 = list(map(template2, filter(filter1, lst1)))  # функция filter
print(lst7)
