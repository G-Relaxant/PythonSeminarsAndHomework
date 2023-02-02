"""
2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

Примеры/Тесты:
10 ->
1
2
4
8

(*) Усложнение. Вывод оформить в одну строку: числа выводить через запятую. Для этого воспользоваться параметрами функции print

Примеры/Тесты:
10     -> 1,2,4,8,
10000  -> 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,
"""

# strng = ''
# a = int(1)
# b = int(2)
# c = int(3)
# strng += str(a)
# print(strng)
# strng += str(b)
# print(strng)
# strng += str(c)
# print(strng)



n = int(input('Введите число N: '))
ans = ''
s = 0
calc = 2**s

for i in range(n):
    if calc < n:
        ans += f'{str(calc)}'
    elif calc == 1:
        ans = '1'
        break
    elif calc == n:
        ans += f', {str(calc)}'
        break
    s += 1
    calc = 2**s
    if calc < n:
        ans += ', '
    elif calc > n:
        break

# ansC = len(ans) - 2
# ans[ansC] = ' '       #почему то так не работает) TypeError: 'str' object does not support item assignment   не понятно, почему он не может перезаписать символы в строке

print(ans)
