year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:                        # Классическое ветвление
    print('YES')
else:
    print('NO')

print('YES' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 'NO')  # Тернарное ветвление


condition1 = year % 4 == 0 and year % 100 != 0
condition2 = year % 400 == 0
print('YES' if condition1 or condition2 else 'NO')                              # Тернарное ветвление с вынесением условий в переменные(аккумуляторы)
