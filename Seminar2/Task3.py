# Fibonacci

#SeminarVariant

# a = int(input())
# if a == 0:
#     print(1)
# else:
#     fib_prev, fib_next = 0,1
#     n = 2
#     while fib_next <= a:
#         if fib_next == a:
#             print(n)
#             break
#         fib_prev, fib_next = fib_next, fib_prev + fib_next
#         n += 1
#     else:                                                      # не понятно, как у вайла может быть элс, што ты такойэ
#         print(-1)



#MyVariant

a = int(input())
fibPrev = 0
fibCurr = 1
counter = 1

if a <= fibCurr:
    if a == fibCurr:
        print('Число А находится на 1м и 2м месте последовательности Фибоначчи')
    else:
        print('Число А равно 0, которое либо находится на 0 месте в последовательности Фибоначчи, либо не входит в эту последовательность')

while a > fibCurr:
    fibBufer = fibCurr
    fibCurr = fibCurr + fibPrev
    print(f'FFiibboonnaaccii ;-){fibCurr}(-:')
    fibPrev = fibBufer
    counter += 1
    if fibCurr == a:
        print(f'Число А находится на {counter} месте в последовательности Фибоначчи')
        print(f'gracia perfecto italiano capuccino')
        break
    elif fibCurr > a:
        print('Число А не входит в последовательность Фибоначчи')
        break
