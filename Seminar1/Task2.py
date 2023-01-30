ych1 = int(input())
ych2 = int(input())
ych3 = int(input())
if ych1 // 2 == 0:
    ychPar = ych1 // 2
else:
    ychPar = ych1 // 2 + 1

par2 = ych2 // 2
par3 = ych3 // 2
sumPar = ychPar + par2 + par3
print(sumPar)
