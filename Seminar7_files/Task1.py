from pathlib import Path            #\
MAIN_DIR = Path(__file__).parent    # | задаём главную(корневую) папку для пути обращения(поиска) к файлу
print()
# fileRead = open('data2.txt', mode = 'r', encoding = 'utf-8')      # OPEN-CLOSE как правило не используется или используется в особенных случаях,
# for line in fileRead:                                             # вместо o-c используют блок WITH OPEN(str25), так как o-c блокирует файл до момента
#     print(line.strip().split('#'))                                # команды close, которая может не сработать из-за ошибки программы, а w-o разблокирует
# fileRead.close()                                                  # файл в любом случае по факту выхода из блока with(даже в случае сбоя программы)


# fileRead = open('data2.txt', mode = 'r', encoding = 'utf-8')
# result = []
# for line in fileRead:
#     result.append(line.strip().split('#'))
# fileRead.close()
# for el in result:
#     print(*el)


fileRead = open(MAIN_DIR / 'data2.txt', mode = 'r', encoding = 'utf-8')     # main_dir - корневая(начальная) папка, от которой далее задаётся путь к файлу(в данном случае файл в корневой папке)
result = []
for line in fileRead:
    tmp = line.strip().split('#')
    result.append(tmp)
    print(*tmp)         # * - распаковка списка в строки
fileRead.close()

print()

with open(MAIN_DIR / 'data2.txt', mode = 'r', encoding = 'utf-8') as fileRead:         # блок WITH OPEN наиболее предпочтителен при работе с файлами
    result = []
    for line in fileRead:
        tmp = line.strip().split('#')
        result.append(tmp)
        print(*tmp)

print()

with open(MAIN_DIR / 'data.txt') as fileRead:
    strPrnt = set(fileRead)
    print(strPrnt)
