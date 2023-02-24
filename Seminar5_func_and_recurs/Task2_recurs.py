"""
Требуется найти N-ое число Фибоначчи через рекурсию
"""



def fib_func(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_func(n-1) + fib_func(n-2)
print(fib_func(0))
print(fib_func(2))
print(fib_func(9))
