
from time import perf_counter
from random import randint

def diffSet(l1: list, l2: list) -> list:  # работа со множествами(set) примерно в 100 раз эффективнее(быстрее), чем со списками
    t1 = perf_counter()                     # time catch start 1
    newSet = set(l1).difference(set(l2))
    t2 = perf_counter()                     # time catch end 1
    return list(newSet), t2-t1

def diffList(l1: list, l2: list) -> list:
    t1 = perf_counter()                     # time catch start 2
    result = []
    for element in l1:
        if element not in l2:
            result.append(element)
    t2 = perf_counter()                     # time catch end 2
    return result, t2-t1

n = 10000
lst1 = [randint(0,int(n)) for i in range(n)]
lst2 = [randint(0,int(n)) for i in range(n)]
rslt, rsltTime = diffList(lst1, lst2)

print(diffSet(lst1, lst2)[1])
#print(rslt)
#print(rsltTime)
print()
print(diffList(lst1, lst2)[1])  # распечатка второго возвращаемого элемента с индексом 1, так как функция возвращает кортеж из двух элементов
