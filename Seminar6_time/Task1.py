lst1 = [23,1,5,12,67,2,3]
lst1copy = lst1

print(lst1)
print(sorted(lst1))     #функция sorted не изменяет аргумент(список)
print()

print(lst1)
lst2 = sorted(lst1)
print(lst2)
print()

print(lst1)
lst1.sort()             #метод .sort изменяет объект(список)
print(lst1)
print()

print(lst1copy.sort())  #None, но список изменился
print(lst1copy)
print()
print()

strng = 'SSDassassdisk'
print(strng.upper())
strng2 = strng.upper()
print(strng)
print(strng2)
print()
print()

def test(x, y):
    return x+y, x-y, x*y    #функция возвращает кортеж
def test2(x, y):
    return[x+y, x*y]        #функция возвращает список
def test3(x, y):
    return x*y, x**y, (1,2,3), [1,'two',"три",(4)], 'olala', True, type(True)
print(test(2,1))
print(test2(2,3))
print(test3(3,4))
print()

a,b,c,d,e,f,g = test3(4,5)  # РАСПАКОВКА, важно чтобы количество переменных соответсвовало колву возвращаемых объектов
print(a,b,c,d,e,f,g)
print(a,b,a,c,d,a,f,f,g,d,e,b,'pinkChocolateByMrMasterMeisterWillyWonka')