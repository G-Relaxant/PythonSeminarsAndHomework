# Factorial

n = int(input())
factorial = 1

# if n == 0:
#     print(factorial)
# else:
#     i = 1
#     while i <= n:             # WHILE
#         factorial *= i
#         i += 1
#     print(factorial)


# if n == 0:
#     print(factorial)
# else:
#     r = range(n)
#     for i in r:               # FOR 1
#         factorial *= i + 1
#     print(factorial)


if n == 0:
    print(factorial)
else:
    for i in range(1, n + 1):   # FOR 2
        factorial *= i
    print(factorial)
