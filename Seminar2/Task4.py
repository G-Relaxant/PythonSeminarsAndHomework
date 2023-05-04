#Вычислить максимальную длительность(непрерывную, без минусов) плюсовых дней за рассматриваемый период

num_days = int(input('Введите количество дней: '))

if 1 <= num_days <= 100:
    curr_day = 0
    length_warm = 0
    max_length_warm = 0
    while curr_day < num_days:
        curr_temp = int(input('Введите температуру: '))
        curr_day += 1
        if curr_temp >= 0:
            length_warm += 1
            if curr_day < num_days - 1 and length_warm > max_length_warm:
                max_length_warm = length_warm
        elif length_warm > max_length_warm:
            max_length_warm = length_warm
            length_warm = 0
print(max_length_warm)
