# ДЛЯ НАТУРАЛЬНОГО N СОЗДАТЬ СПИСОК, СОСТОЯЩИЙ ИЗ ЭЛ-ТОВ ПОСЛЕДОВАТЕЛЬНОСТИ 3N + 1
# ПРИМЕР N = 6: [1, 4, 7, 10, 13, 16, 19]


#Variant1
# n = 6
# lst1 = []

# for idx in range(n+1):
#     lst1.append(3 * idx + 1)

# print(lst1)



#Variant2
n = 6
# # lst1 = [0] * (n + 1)          # классический вид
# lst1 = [0 for i in range(n+1)]  # вид comprehension
# for idx in range(n + 1):
#     lst1[idx] = 3 * idx + 1

# print(lst1)

# print([(3 * i + 1) for i in range(n+1)])    # вид comprehension


# Variant3   Ячейка списка, соответствующая последовательности по условию, принимает значение индекса. Печать всего списка
lst1 = [0] * (3*n+2)
for i in range(n+1):
    lst1[3*i+1] = 3*i+1
print(lst1)
# [0,1,0,0,4,0,0,7,0,0,10]



# Variant4
list1 = [0]

for i in range(n+1):
    list1.append(3*i+1)
    list1.append(0)
    list1.append(0)
list1.pop()
list1.pop()
print(list1)
