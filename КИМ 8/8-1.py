from itertools import*
from string import*
a = 0
for i in product(printable[:5],repeat = 6):
    i = ''.join(i)
    if i[-1] != '3' and i[-1] != '4' and i[0] != '1' and i[0] != '0':
        a += 1
print(a)

'''from itertools import*
a = 0
for i in product(sorted('епсух'), repeat = 5):
    i = ''.join(i)
    if i[-1] == 'п' or i[-1] == 'с' or i[-1] == 'х':
        a += 1
    if i == 'успех':
        print(a)'''

'''a = 0
for x in range(0,101):
    for y in range(0,101):
        for z in range(0,101):
            for w in range(0,101):
                if 1*x + 2*y + 5*z + 10*w == 100:
                    a +=1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('режимдно'), repeat = 6):
    i = ''.join(i)
    if len(i) == len(set(i)):
        i = i.replace('р','s')
        i = i.replace('е','g')
        i = i.replace('ж','s')
        i = i.replace('и','g')
        i = i.replace('м','s')
        i = i.replace('д','s')
        i = i.replace('н','s')
        i = i.replace('о','g')
        if i[0] == 's' and i[1] == 'g' and i[-1] == 'g':
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('инфа'), repeat = 6):
    i = ''.join(i)
    if i.count('ф') == 2:
        a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('левиоса'), repeat = 7):
    i = ''.join(i)
    if len(i) == len(set(i)):
        i = i.replace('л','s')
        i = i.replace('е','g')
        i = i.replace('в','s')
        i = i.replace('и','g')
        i = i.replace('о','g')
        i = i.replace('с','s')
        i = i.replace('а','g')
        if i[0] != 'g' and i[3] != 's':
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('гафний'), repeat = 4):
    i = ''.join(i)
    if i[0] != 'й':
        i = i.replace('г','s')
        i = i.replace('а','g')
        i = i.replace('ф','s')
        i = i.replace('н','s')
        i = i.replace('и','g')
        i = i.replace('й','s')
        if i.count('g') >= 1:
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('крот'), repeat = 6):
    i = ''.join(i)
    if i.count('о') == 1:
        a += 1
print(a)'''

'''from itertools import*
from string import*
a = 0
for i in product(printable[:8], repeat = 5):
    i = ''.join(i)
    if i.count('6') == 1 and i[0] != '0':
        for z in '1357':
            if f'{z}6' in i or f'6{z}' in i:
                break
        else:
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('паште'),repeat = 4):
    if i[0] in 'пшт' and i[2] in 'пшт' and i[1] in 'ае' and i[3] in 'ае' and i.count('п') == 1:
        a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('чето'), repeat = 6):
    if i.count('е') >= 1:
        a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('kiten'),repeat = 5):
    if i[0] not in 'ie' and i[-1] not in 'ktn':
        a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('абвгде'),repeat = 4):
    if i[0] not in 'бвгд' and i[-1] not in 'ае':
        a += 1
print(a)'''

'''from itertools import*
a = 0
for z in permutations(sorted('домище'),r = 5):
    i = ''.join(z)
    i = i.replace('д','s')
    i = i.replace('о','g')
    i = i.replace('м','s')
    i = i.replace('и','g')
    i = i.replace('щ','s')
    i = i.replace('е','g')
    if 'ss' not in i and 'gg' not in i and i[0] == 's':
        a += 1
print(a)'''

'''from itertools import*
a = 0
for i in permutations(sorted('школа'),r = 5):
    if 'аш' not in ''.join(i) and 'ша' not in ''.join(i):
        a += 1
print(a)'''

'''from itertools import*
a = 0
for i in permutations(sorted('0123456789'),r = 6):
    numb = ''.join(i)
    if int(numb)%5 == 0 and numb[0] != '0':
        numb  = numb.replace('0','0')
        numb  = numb.replace('1','1')
        numb  = numb.replace('2','0')
        numb  = numb.replace('3','1')
        numb  = numb.replace('4','0')
        numb  = numb.replace('5','1')
        numb  = numb.replace('6','0')
        numb  = numb.replace('7','1')
        numb  = numb.replace('8','0')
        numb  = numb.replace('9','1')
        if '11' not in numb and '00' not in numb:
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in permutations(sorted('0123456789'),r = 5):
    numb = ''.join(i)
    if int(numb)%5 == 0 and numb[0] != '0':
        numb  = numb.replace('0','0')
        numb  = numb.replace('1','1')
        numb  = numb.replace('2','0')
        numb  = numb.replace('3','1')
        numb  = numb.replace('4','0')
        numb  = numb.replace('5','1')
        numb  = numb.replace('6','0')
        numb  = numb.replace('7','1')
        numb  = numb.replace('8','0')
        numb  = numb.replace('9','1')
        if '11' not in numb and '00' not in numb:
            a += 1
print(a)'''

'''from itertools import*
a = 0
for i in product(sorted('345678'),repeat = 7):
    if i.count('5') == 2:
        a += 1
print(a)'''

'''from itertools import*
a = 0
for z in product(sorted('skate'),repeat = 5):
    i = ''.join(z)
    if i.count('t') <= 1 and i[0] != 't' and i[-1] != 't' and 'ta' not in i and 'at' not in i:
        a += 1
print(a)'''

'''from itertools import*
a = 0
for z in product(sorted('01234567'),repeat = 5):
    i = ''.join(z)
    i = i.replace('1','*')
    i = i.replace('3','*')
    i = i.replace('5','*')
    i = i.replace('7','*')
    if ('4*' not in i) and ('*4' not in i) and i.count('4') == 2 and i[0] != '0':
        a += 1
print(a)'''

'''from itertools import*
a = 0
for z in permutations(sorted('0123456789'),r = 8):
    i = ''.join(z)
    if i[0] != '0':
        i = i.replace('1','1')
        i = i.replace('2','0')
        i = i.replace('3','1')
        i = i.replace('4','0')
        i = i.replace('5','1')
        i = i.replace('6','0')
        i = i.replace('7','1')
        i = i.replace('8','0')
        i = i.replace('9','1')
        i = i.replace('0','0')
        if '11' not in i and '00' not in i:
            a += 1
print(a)'''

'''from itertools import*
a = 0
for z in product(sorted('01234567'),repeat = 4):
    i = ''.join(z)
    if i[0] != '0' and i[0] not in '0246' and i[-1] not in '07' and i.count('5') <= 1:
        a += 1
print(a)'''

'''from itertools import*
from string import*
a = 0
for z in product(printable[:15],repeat = 6):
    i = ''.join(z)
    if i[0] != '0' and i.count('0') > 2 and i[-1] == '9' and '23' not in i:
        a += 1
print(oct(a)[2:])'''

'''from itertools import*
a = 0
for z in set(permutations(sorted('малина'),r = 5)):
    i = ''.join(z)
    if 'аа' not in i:
        a += 1
print(a)'''

'''from itertools import*
a = 0
for z in permutations(sorted('0123456789'),r = 3):
    i = ''.join(z)
    if i[0] != '0':
        i = i.replace('1','1')
        i = i.replace('2','0')
        i = i.replace('3','1')
        i = i.replace('4','0')
        i = i.replace('5','1')
        i = i.replace('6','0')
        i = i.replace('7','1')
        i = i.replace('8','0')
        i = i.replace('9','1')
        i = i.replace('0','0')
        if '11' not in i and '00' not in i:
            a += 1
print(a)'''

'''from itertools import*
from string import*
a = 0
for z in product(printable[:5],repeat = 4):
    i = ''.join(z)
    if i[0] != '0' and i[0] > i[1] and i[1] > i[2] and i[2] > i[3]:
        a += 1
print(a)'''

'''from itertools import*
from string import*
a = 0
for z in product(printable[:7],repeat = 6):
    i = ''.join(z)
    if i[0] != '0' and i[0] not in '135' and i[-1] not in '34' and i.count('5') <= 1:
        a += 1
print(a)
'''

'''from itertools import*
from string import*
a = 0
for z in permutations(printable[:12],r = 9):
    i = ''.join(z)
    if i[0] != '0' and int(i,12) % 2 != 0:
        i = i.replace('0','*')
        i = i.replace('2','*')
        i = i.replace('4','*')
        i = i.replace('6','*')
        i = i.replace('8','*')
        i = i.replace('a','*')
        if i.count('*') == 5:
            a += 1
print(a)'''