f = open('сюда вставить файл')
a = [] # a = [int(s) for s in f]
for s in f:
    a.append(int(s))
sumpar = []
for i in range(len(a) - 1):
    if a[i] % 11 == 0 and a[i+1] % 11 == 0:
        sumpar.append(a[i] + a[i+1])
print(len(sumpar), min(sumpar))

'''f = open('17.1-файл') # Сначала вставить файл в папку номеров 17, потом в кавычках вставить название сюда
a = [int(s) for s in f] # Переписывает числа из файла в список, чтобы дальше было удобно работать
sumpar = [] # Пустой список сумм пар чисел
for i in range(len(a)-1): # Перебираем значения по индексам за исключением последнего: у него пары нет, вылезет ошибка
    if a[i] % 8 == 0 and a[i+1] % 8 == 0: # Условия для числа с инлексом i и следующим (с индексом i+1)
        sumpar.append(abs(a[i]-a[i+1])) # В список сумм пар добавляется значение по условию. Количество значений будет равно количеству пар
print(len(sumpar), min(sumpar))'''

'''f = open('17.2-file')
a = [int(s) for s in f]
s = []
for i in range(len(a)-1):
    if a[i] > 500 or a[i+1] > 500:
        s.append(a[i]**2 + a[i+1]**2)
print(len(s), max(s))'''

'''f = open('17.3-file')
a = [int(s) for s in f]
sum = []
for i in range(len(a)-2):
    if a[i] < 0 or a[i+1] < 0 or a[i+2] < 0:
        sum.append(a[i] + a[i+1] + a[i+2])
print(len(sum),min(sum))'''

'''f = open('17.4-file')
a = [int(s) for s in f]
sum = []
for i in range(len(a)-1):
    if (a[i] > 0 and a[i]**(1/2) % 1 == 0) or (a[i+1] > 0 and a[i+1]**(1/2) % 1 == 0):
        sum.append(a[i] + a[i+1])
print(len(sum), max(sum))'''

'''f = open('17.5-file')
a = [int(s) for s in f]
sum = []
for i in range(len(a)-1):
    if (a[i]**2 + a[i+1]**2) > 80 and (a[i]**2 + a[i+1]**2) % 2 == 0:
        sum.append(a[i]**2 + a[i+1]**2)
    if a[i]**2 + a[i+1]**2 == 6664:
        d = max(a[i], a[i+1])
print(len(sum), d)'''

'''f = open('17.6-file')
a = [int(s) for s in f]
sum = []
for i in range(len(a)-1):
    if abs(a[i]) + abs(a[i+1]) > 650:
        sum.append(max(a[i], a[i+1]))
print(len(sum), max(sum))'''

'''f = open('17-7.txt')
a = [int(s) for s in f]
sumpar = []
for i in range(len(a) - 1):
    if (abs(a[i]) % 123 == min(a)) or (abs(a[i+1]) % 123 == min(a)):
        sumpar.append(a[i] + a[i + 1])
print(len(sumpar), max(sumpar))'''

'''f = open('17-8.txt')
a = [int(s) for s in f]
sumpar = []
makn = max([x for x in a if x % 2 == 1])
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) == makn:
        sumpar.append((a[i]**2 + (a[i+1]**2)))
print(len(sumpar), max(sumpar))'''

'''f = open('17-9.txt')
a = [int(s) for s in f]
sumpar = []
sr = sum(a)/len(a)
for i in range(len(a) - 1):
    if ((a[i] > sr) or (a[i+1] > sr)) and ((a[i] % 7 == 0) or (a[i + 1] % 7 == 0)):
        sumpar.append(a[i] * a[i+1])
print(len(a), max(sumpar))'''

'''f = open('17-10.txt')
a = [int(s) for s in f]
sumpar = []
min2 = min([x for x in a if 9 < x < 100])
for i in range(len(a) - 1):
    if (((99 < a[i] < 1000) +(99 < a[i+1] < 1000)) == 1) and ((a[i] + a[i+1]) % min2 == 0):
        sumpar.append(a[i] + a[i+1])
print(len(sumpar), max(sumpar))'''

'''f = open('17.7.txt')
a = [int(s) for s in f]
sumpar = []
for i in range(len(a) - 1):
    x = -100000000
    y = -100000000
    if 999 < a[i] < 10000 and a[i] % 100 == 43:
        x = a[i]
    if 999 < a[i+1] < 10000 and a[i+1] % 100 == 43:
        y = a[i+1]
    if (999 < a[i] < 10000 or 999 < a[i+1] < 10000) and ((a[i] + a[i+1])**2 < (max(x,y))**2):
        sumpar.append((a[i] + a[i+1])**2)
print(len(sumpar), max(sumpar))'''

'''f = open('17-9.txt')
a = [int(s) for s in f]
sumpar = []
sr = sum(a)/len(a)
for i in range(len(a) - 1):
    if ((a[i] > sr) or (a[i+1] > sr)) and ((a[i] % 7 == 0) or (a[i + 1] % 7 == 0)):
        sumpar.append(a[i] * a[i+1])
print(len(a), max(sumpar))'''

'''f = open('17-11.txt')
a = [int(s) for s in f]
sumpar = []
sr = max([z for z in a if (999<z<10000 and z % 100 == 43)])
for i in range(len(a) - 1):
    if (999<abs(a[i])<10000 or 999<abs(a[i+1])<10000) and ((a[i] + a[i+1])**2 < sr**2):
        sumpar.append((a[i] + a[i+1])**2)
print(len(sumpar), max(sumpar))'''

'''f = open('17-12.txt')
a = [int(s) for s in f]
sumpar = []
min123 = min([int(s) for s in a if abs(s) % 123 == 0 and s > 0])
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) < min123:
        sumpar.append(a[i] + a[i + 1])
print(len(sumpar))
print(max(sumpar))'''

