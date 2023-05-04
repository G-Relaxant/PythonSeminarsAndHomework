#Variant1
text = "She   sells     sea  shells        on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
print(text.split(" "))
print(text.split())    # без указанного разделителя для сплита, любое количество последовательных пробелов принимается за разделитель

print(len(set(text.split())))



#Variant2 
text = "She   sells     sea  shells        on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
result = []
text = text.split()
for i in text:
    if i.lower() not in result:
        result.append(i)
print(len(result))
