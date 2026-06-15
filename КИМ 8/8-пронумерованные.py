'''len(i) == len(set(i))''' #Проверка на все разные буквы

from itertools import* #Импорт библиотеки
a = 0 #Ввод вспомогательной переменной
for i in product(sorted('чистыйразум'), repeat = 5): #В product указывается сначала набор символов в алфавитном порядке или отсортированными с помощью sorted, если нет ё, потом repeat = кол-во символов
    i = ''.join(i) #Склейка символов в единое слово
    if i.count('й') <= 1: #Условие: в слове 1 или 0 букв й
        a += 1
print(a)

'''from itertools import*
a = 0
z = 0
for i in product(sorted('солнце'), repeat = 6):
    i = ''.join(i)
    a += 1
    if a % 2 == 0 and i[0] != 'о' and i[0] != 'е' and i.count('ц') == 2:
        z += 1
print(z)'''

'''from itertools import*
a = 0
for i in product(sorted('алгоритм'), repeat = 4):
    i = ''.join(i)
    a += 1
    if i[-2] == 'и' and i[-1] == 'м':
        print(a,i)'''

'''from itertools import*
a = 0
z = 0
for i in product(sorted('лето'), repeat = 4):
    i = ''.join(i)
    a += 1
    if i.count('е') >= 1:
        z += 1
print(z)'''

'''from itertools import*
a = 0
z = 0
for i in product(sorted('гафний'), repeat = 4):
    i = ''.join(i)
    a += 1
    if i[0] != 'й' and (i.count('а') > 0 or i.count('и') > 0):
        z += 1
print(z)'''

'''from itertools import*
a = 0
z = 0
for i in product(sorted('сало'), repeat = 6):
    i = ''.join(i)
    a += 1
    if 1 <= i.count('о') <= 3:
        z += 1
print(z)'''

'''from itertools import*
a = 0
z = 0
for i in product(sorted('теория'), repeat = 6):
    i = ''.join(i)
    a += 1
    if a % 2 != 0 and i[0] != 'р' and i[0] != 'т' and i[0] != 'я' and i.count('и') >= 2:
        print(a,i)'''

'''from itertools import*
a = 0
z = 0
for i in product(sorted('ав123'), repeat = 8):
    i = ''.join(i)
    a += 1
    if i.count('а') + i.count('в') == 2:
        z += 1
print(z)'''

'''from itertools import*
a = 0
z = 0
for i in product(sorted('калий'), repeat = 6):
    i = ''.join(i)
    a += 1
    if i.count('й') <= 1 and i[0] != 'й' and i[-1] != 'й' and i.count('ий') == 0 and i.count('йи') == 0:
        z += 1
print(z)'''

'''from itertools import*
a = 0
z = 0
for i in product(sorted('гранит'), repeat = 6):
    i = ''.join(i)
    a += 1
    if a % 2 != 0 and i[0] != 'а' and i[0] != 'и' and i[0] != 'г' and i.count('а') == 1:
        print(a,i)'''

'''from itertools import*
a = 0
for i in product(sorted('кофе'), repeat = 5):
    i = ''.join(i)
    a += 1
    if i.count('о') == 1 and i.count('ок') == 0 and i.count('ко') == 0 and i.count('оф') == 0 and i.count('фо') == 0:
        print(a,i)'''

'''from itertools import*
a = 0
z = 0
for i in product(sorted('запись'), repeat = 6):
    i = ''.join(i)
    a += 1
    if len(i) == len(set(i)) and i[0] != 'ь' and i.count('аь') == 0 and i.count('иь') == 0:
        z += 1
print(z)'''

'''from itertools import*
a = 0
for i in product(sorted('апрель'),repeat = 6):
    i = ''.join(i)
    a += 1
    if a % 2 != 0 and i[0] != 'а' and i[0] != 'л' and i.count('п') >= 2:
        print(a)
        break'''

'''from itertools import*
a = 0
for i in product(sorted('щэдср'), repeat = 4):
    i = ''.join(i)
    a += 1
    if i == 'щдщд':
        print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('марин'), repeat = 8):
    i = ''.join(i)
    a += 1
    if i == 'марианна':
        print(a)'''


'''from itertools import*
a = 0
for i in product(sorted('автор'), repeat = 4):
    i = ''.join(i)
    a += 1
    if i == 'вата':
        print(a)'''

'''from itertools import*
a = 0
for i in product('геэ023', repeat = 7):
    i = ''.join(i)
    a += 1
    if i == 'егэ2023':
        x = a
    if i == '2023егэ':
        y = a
print(abs(x-y)-1)'''

'''from itertools import*
a = 0
for i in product(sorted('пятьдней'), repeat = 4):
    i = ''.join(i)
    a += 1
    if len(i) == len(set(i)):
        i = i.replace('п','s')
        i = i.replace('я','g')
        i = i.replace('т','s')
        i = i.replace('ь','s')
        i = i.replace('д','s')
        i = i.replace('н','s')
        i = i.replace('е','g')
        i = i.replace('й','s')
        if i.count('g') == 0:
            print(a,i)'''

'''from itertools import*
a = 0
for i in product(sorted('ауе'),repeat = 5):
    word = ''.join(i)
    a += 1
    if a == 222:
        print(word)'''

'''from itertools import*
a = 0
for i in product(sorted('пейзаж'),repeat = 5):
    word = ''.join(i)
    a += 1
    if word[0] != 'п' and word.count('ж') == 3 and word.count('а') <= 2:
        print(a,word)'''

'''from itertools import*
a = 0
z = 0
for i in product(sorted('вебинар'),repeat = 6):
    word = ''.join(i)
    a += 1
    if a%2==0 and word[0] != 'е'and word.count('р') == 2:
        z += 1
print(z)'''

'''from itertools import*
a = 0
for i in product(sorted('уперс'),repeat = 5):
    word = ''.join(i)
    a += 1
    if a%2!=0 and word[0] not in 'еу' and word.count('с') == 3:
        print(a,word)'''

'''from itertools import*
a = 0
for i in product(sorted('машин'),repeat = 5):
    word = ''.join(i)
    a += 1
    if word.count('а') == 3 and word.count('ш') == 0 and word.count('мм') == 0: 
        print(a,word)'''



