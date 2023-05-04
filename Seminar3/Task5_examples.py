lst1 = [11,22,43,74,5,68,7,88,90]

# for idx in range(len(lst1)):
#     if lst1[i] > lst[i-1]:        # что дальше и где lst непонятно


# for el in lst1:
#     print(el)


# for idx, el in enumerate(lst1):
#     print(f"lst1[{idx}] = {el}")


dict1 = {1:"sdsd", 2:"12121"}
for key in dict1.keys():
    print(key)
print("-"*12)
for value in dict1.values():
    print(value)
print("-"*12)

for key, value in dict1.items():
    print(f"dict1[{key}] = {value}")
