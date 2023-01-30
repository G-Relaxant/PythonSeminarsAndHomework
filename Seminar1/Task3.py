man1 = 21
if man1 % 2 == 0:
    count1 = man1 // 2
else:
    count1 = man1 // 2 + 1

count1 = man1 // 2 if man1 % 2 == 0 else man1 // 2 + 1  #\
count2 = man1 // 2 if man1 % 2 == 0 else man1 // 2 + 1  # | ТЕРНАРНЫЙ ОПЕРАТОР - запись ветвления if-else в одну строку, если код каждой ветки занимает не более 1 строки
count3 = man1 // 2 if man1 % 2 == 0 else man1 // 2 + 1  #/
