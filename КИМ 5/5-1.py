'''#Эта функция вставляется в номера 5 для перевода в нестандартную систему счисления
def f(n,k): #Ф-ция, переводящая число n из 10-ной в k-ную
    s = '' #Пустая строка, в которую записываюся остатки от деления
    while n > 0:
        s = str(n%k) + s #Остатки приписываются слева, поэтому числа уже расположены в правильном порядке
        n //= k #После нахождения остатка делим число на основание системы
    return s'''

for n in range(1,10000): # Перебор входных данных
    n2 = bin(n)[2:] # Перевод в новую систему по условию
    if n%2!=0: # Проверка на условия по условию
        n2 = '10' + n2
    else:
        n2 = '1' + n2 + '10'
    R = int(n2,2) # Результат работы программы в десятичной системе
    if R > 697: # Финальное условие
        print(n)
        break

'''for n in range(1,10000):
    n2 = bin(n)[2:]
    if n % 5 == 0:
        n2 += n2[-3:]
    else:
        n2 += bin((n%5)*5)[2:]
    R = int(n2,2)
    if R > 256:
        print(n)
        break'''

'''a = []
for n in range(1,10000):
    n2 = bin(n)[2:]
    if n % 3 == 0:
        n2 += n2[-3:]
    else:
       n2 += bin((n % 3) * 3)[2:]
    R = int(n2,2)
    if R == 134:
        a.append(n)
print(max(a))'''

'''q = []
for n in range(10000,100000):
    a = [int(x) for x in str(n)]
    s = sum(a)
    m = max(a) + min(a)
    l = a[0]
    r = a[-1]
    p1 = s - l
    p2 = m - r
    if p1>p2:
        z = str(p2) + str(p1)
    else:
        z = str(p2) + str(p1)
    if z == '222':
        q.append(n)
print(max(q))
'''

'''a = []
for n in range(1,10000):
    n2 = bin(n)[2:]
    n2 += str(n2.count('1') % 2)
    n2 += str(n2.count('1') % 2)
    R = int(n2,2)
    if R > 396:
        a.append(R)
print(min(a))'''

'''a = []
for n in range(1,13):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = '10' + n2
    else:
        n2 = '1' + n2 + '01'
    r = int(n2,2)
    a.append(r)
print(max(a))'''

'''a = []
for n in range(1,10000):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 = '10' + n2[2:] + '0'
    else:
        n2 = '11' + n2[2:] + '1'
    r = int(n2,2)
    if r <= 19:
        a.append(n)
print(max(a))
'''