#Они сложные только из-за дурацких формулировок, нужно внимательно читать что дано в задании и что нужно найти
for n in range(123456,123487+1): #В условии дан диапазон, переписываем его, добавляя 1 к концу, чтобы значение включилось в перебор
    deliteli = []
    for i in range(1,n+1): #Перебираем числа от 1 до самого числа включительно
        if n % i == 0: #Если число без остатка делится на i...
            deliteli.append(i) #То это делитель, записываем его в список
    if len(deliteli) == 6: #Если у числа нашлось 6 делителей...
        print(deliteli) #Выводим их, как просят в задании

'''for n in range(15545,15844 +1):
    deli = []
    for i in range(2,n): #Иногда нужно перебирать делители не включая 1 и само число, поэтому начинаем перебор с 2 и не добавляем 1 к числу
        if n % i == 0:
            deli.append(i)
    if len(deli) == 5:
        print(n,max(deli))'''

'''c = 0
for n in range(950001,950001+1000): #Когда просят перебрать числа больше н-ного, перебираем 1000 чисел после него, не включая само число
    F = 0 #Значение дополнительной переменной поясняется в задании
    for i in range(2,n):
        if n % i == 0:
            F = n//i - i #Тут F = разница между мин и макс делителями числа. Находим сначала мин делитель, делин число на него, получаем максимальный
            break
    if F != 0 and F % 13 == 0:
        print(n,F)
        c += 1
    if c == 5: #Нам нужно только первые 5 подходящих случаев, вводим обычный счетчик
        break'''

'''def isprime(x): #Для упрощения некоторых задач лучше отдельно написать ф-цию. Эта проверяет число на простоту
    for i in range(2,x): #Перебираем числа, не включая 1 и само число
        if x % i == 0: #Если нашелся делитель...
            return 0 #Число не простое
    return 1 #Если ничего не нашлось, значит простое
c= 0
for n in range(1000001,1000001+1000):
    for i in range(2,n):
        if n % i == 0:
            if isprime(n//i):
                print(n,n//i)
                c+=1
            break #Break должен стоять именно тут, это важно
    if c == 5:
        break'''

'''c = 0
for n in range(800001, 800000+1000):
    for i in range(111,n,100): #Если делитель должен кончаться на определенные цифры, нужно делать такой перебор с шагом. Тут для числа 11
        if n % i == 0:
            print(n,i)
            c += 1
            break
    if c == 5:
        break'''

'''c = 0
for n in range(800001,800001 + 1000):
    deli = []
    for i in range(2,n):
        if n % i == 0:
            deli.append(i)
    F = 0
    if len(deli) > 1:
        F = deli[0] * deli[-2]
    if F != 0 and F % sum(deli[:2]) == 0:
        print(n,F)
        c += 1
    if c == 5:
        break'''

'''for n in range(200123,200150+1):
    deli = []
    for i in range(1,n+1):
        if n % i == 0:
            deli.append(i)
    if len(deli) == 4:
        print(n,sum(deli)/4)'''

'''for n in range(14620,15000+1):
    deli = []
    for i in range(2,n):
        if n % i == 0:
            deli.append(i)
    if len(deli) == 3:
        print(n,min(deli))'''

'''c = 0
for n in range(700001,700001+1000):
    F = 0
    for i in range(2,n):
        if n % i == 0:
            F = n//i - i
            break
    if F != 0 and F % 9 == 0:
        print(n,F)
        c += 1
    if c == 5:
        break'''

'''c = 0
for n in range(600001,600001+1000):
    for i in range(17,n,10):
        if n % i == 0:
            print(n,i)
            c += 1
            break
    if c == 5:
        break'''

'''c = 0
def isprost(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1
for n in range(610001,610001+1000):
    for i in range(2,n):
        if n % i == 0:
            if isprost(n//i):
                print(n,n//i)
                c += 1
            break
    if c == 6:
        break'''

'''for x in range(200123,200150+1):
    deliteli = []
    for d in range(1, x+1):
        if x % d == 0:
            deliteli.append(d)
    if len(deliteli) == 4:
        print(x,deliteli)'''

'''for x in range(23456,78954+1):
    deli = []
    if ((x**0.5) % 1) == 0:
        for d in range(2,x):
            if x % d == 0:
                deli.append(d)
        if len(deli) == 3:
            print(x,max(deli))'''

'''for x in range(800001,800001 + 100):
    deli = []
    for d in range(17,x,10):
        if x % d == 0:
            print(x,d)
            break'''

'''def isprime(x):
    for d in range(2,int(x**0.5)+1):
        if x % d == 0:
            return False
    return True

for x in range(7800001,7800001+1000000):
    deliprime = []
    for d in range(2,int(x**0.5)+1):
        if x % d == 0:
            if isprime(d):
                deliprime.append(d)
            if isprime(x//d):
                deliprime.append(x//d)
    if len(deliprime) != 0:
        M = max(deliprime)+min(deliprime)
        if M > 100000 and str(M) == str(M)[::-1]:
            print(x,M)'''

'''def isprime(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return str(x).count('4') == 1

for x in range(5555221,5555221+1000):
    for d in range(2,int(x**0.5)+1):
        if x % d == 0:
            if isprime(d) and isprime(x//d):
                print(x, x // d)
                break
'''

'''def isprime(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return str(x).count('3') or str(x).count('6')

for x in range(3646001,3646001+1000):
    for d in range(2,int(x**0.5)+1):
        if x % d == 0:
            if isprime(d) and isprime(x//d):
                print(x, x // d)
                break'''

'''a = []
for y in range(1,10000,2):
    for z in range(1,13):
        x = 105 * y + 3**z
        if len(str(x)) == 6 and str(x).count('3') == 0:
            a.append([x,z])
a.sort()
print(a[:5])'''

'''a = []
for y in range(1,10000,2):
    for z in range(1,13):
        x = 125 * y + 3**z
        if len(str(x)) == 6 and str(x).count('3') == 0:
            a.append([x,z])
a.sort()
print(a[:5])'''


