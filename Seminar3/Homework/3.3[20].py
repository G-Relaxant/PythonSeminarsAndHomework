"""
3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.

Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
которое содержит либо только английские, либо только русские буквы и заранее известно какой алфавит надо использовать.

Примеры/Тесты:
Input:   ноутбук
Output:  12

Input:   notebook
Output:  14

(*) Примечание.
Подумайте о том какие структуры данных здесь наиболее удобно использовать, чтобы просто проверять в какую группу попадает буква, а также
просто накапливать сумму очков.
"""




word1 = input('Введите слово: ')
# word2 = [element.upper() for element in word1] # это просто на память, мб пригодится
word1 = word1.upper()
print(word1)

eng1point = 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'
eng2point = 'D', 'G'
eng3point = 'B', 'C', 'M', 'P'
eng4point = 'F', 'H', 'V', 'W', 'Y'
eng5point = 'K'
eng8point = 'J', 'X'
eng10point = 'Q', 'Z'
rus1point = 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'
rus2point = 'Д', 'К', 'Л', 'М', 'П', 'У'
rus3point = 'Б', 'Г', 'Ё', 'Ь', 'Я'
rus4point = 'Й', 'Ы'
rus5point = 'Ж', 'З', 'Х', 'Ц', 'Ч'
rus8point = 'Ш', 'Э', 'Ю'
rus10point = 'Ф', 'Щ', 'Ъ'

#print(eng1point[3]) #test
#print(word1[0]) #test

checkLang = 0
checkLet = word1[0]
if checkLet in eng1point:
    checkLang = 'eng'
elif checkLet in eng2point:
    checkLang = 'eng'
elif checkLet in eng3point:
    checkLang = 'eng'
elif checkLet in eng4point:
    checkLang = 'eng'
elif checkLet in eng5point:
    checkLang = 'eng'
elif checkLet in eng8point:
    checkLang = 'eng'
elif checkLet in eng10point:
    checkLang = 'eng'
else:
    checkLang = 'rus'
#print(checkLang) #test

pointsSum = 0

if checkLang == 'eng':
    for idx in word1:           # заметка на будущее: idx в данном случае принимает в себя значение символа, и соответственно является типом str, а не int, (но цикловой счёт и перебор всего слова продолжается)
        if idx in eng1point:
            pointsSum += 1
        elif idx in eng2point:
            pointsSum += 2
        elif idx in eng3point:
            pointsSum += 3
        elif idx in eng4point:
            pointsSum += 4
        elif idx in eng5point:
            pointsSum += 5
        elif idx in eng8point:
            pointsSum += 8
        elif idx in eng10point:
            pointsSum += 10
else:
    for idx in word1:
        if idx in rus1point:
            pointsSum += 1
        elif idx in rus2point:
            pointsSum += 2
        elif idx in rus3point:
            pointsSum += 3
        elif idx in rus4point:
            pointsSum += 4
        elif idx in rus5point:
            pointsSum += 5
        elif idx in rus8point:
            pointsSum += 8
        elif idx in rus10point:
            pointsSum += 10

print(f'Result: {pointsSum}')
