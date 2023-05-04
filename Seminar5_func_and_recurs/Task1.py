# def function_name(x, y, z = "assAssDisc"):
#     print(x,y,z)

# function_name(1,2,23)

# function_name(0,2232) # если аргумент не задан, то он берётся из иниц. аргумента

# function_name(13,2,31) # в этом и выше случаях используется Позиционное сопоставление(порядок аргументов в иниц. порядке)

# function_name(y = 13, z = 2, x = 31) # Именованное сопоставление(порядок присвоения аргументов указывается в строке вызова функции)

# print()

# def func_name(x, y, z):
#     if isinstance(y, int):
#         print(x, y, z)
#     elif isinstance(y, str):
#         print(x, y*2, z)
#     return 0.0

# res1 = func_name(1,2,23)
# print(res1)
# func_name(0, 'TCmode', 'shladkiyLolipopchik')

# print()

def func_name(x, y, z = 'votTakV_STANISLA_RemontiruyutAyfoniKurochkaKoshechkaMoyaNya'):
    if isinstance(y, int):
        print(x, y, z)
        return x*y*z
    elif isinstance(y, str):
        print(x, y*2, z)
        return '=0.0='

res1 = func_name(1,2,23)
res2 = func_name(0, 'qwerty')
res3 = func_name(0, True)
res4 = func_name(0, [1,2,3])
print(res1, res2, res3, res4)
