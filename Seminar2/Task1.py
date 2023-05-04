# idx = 3
# while idx <= 9:             # вариант с циклом While
#     print(idx)
#     idx += 2


# for idx in range(3, 10, 2): # вариант с циклом For
#     print(idx)


idx = 0
while idx <= 9:
    idx += 1
    if idx == 7:
        break       #оператор Break останавливает цикл
    if idx == 2:
        continue    #оператор Continue останавливает(пропускает) текущий виток
    print(idx)
