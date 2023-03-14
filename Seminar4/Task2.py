# подсчёт встечаемости каждого элемента в строке

text = 'a a a b c a a d c d d'
text = text.split()
result = ''

d = {}
for i in range(len(text)):
    if text[i] not in d:
        d[text[i]] = 1
    else:
        d[text[i]] += 1
print(d)




#

text = 'a a a b c a a d c d d'
text = text.split()
print(text)
result = ''

d = {}
for i in range(len(text)):
    if text[i] not in d:
        d[text[i]] = 1
        result += f'{text[i]} '
    else:
        d[text[i]] += 1
        result += f'{text[i]}_{d[text[i]] - 1} '
print(result)
