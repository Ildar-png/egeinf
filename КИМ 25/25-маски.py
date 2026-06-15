from fnmatch import* #Импорт библиотеки
for x in range(0,10**8,61): #Перебор чисел от 0 до 10**8 с шагом в 61. Делаем так, чтобы не вводить проверку на деление и оптимизировать прогу
    if fnmatch(str(x),'23456??8'): #На вход в fnmatch подается строка, а потом маска, которую можно переписать прямо из условия теми же знаками
        print(x,x//61) #Выводим число и его частное от деления, как просят в задаче

'''from fnmatch import*
for x in range(0,10**8,63):
    if fnmatch(str(x),'134?3?'):
        print(x,x//63)'''

'''from fnmatch import*
for x in range(0,10**8,2023):
    if fnmatch(str(x),'37*87?'):
        print(x,x//2023)'''

'''from fnmatch import*
for x in range(0,10**8,343):
    if fnmatch(str(x),'51?32*8'):
        print(x,x//343)'''

'''from fnmatch import*
a =[]
for x in range(0,100000,134):
    if fnmatch(str(x),'1?7*'):
        a.append(bin(x)[2:].count('1'))
print(sorted(a))
'''

'''from fnmatch import*
for x in range(0,10**8,98):
    if fnmatch(str(x),'12*678?'):
        print(x,x//98)'''

'''from fnmatch import*
for x in range(0,10**8,31):
    if fnmatch(str(x),'123*578'):
        print(x,x//31)'''

'''from fnmatch import*
for x in range(0,10**10,9874):
    if fnmatch(str(x),'89*6?7?9?'):
        print(x,x//9874)'''

'''from fnmatch import*
for x in range(0,10**8,31):
    if fnmatch(str(x),'123*578'):
        print(x,x//31)'''

'''from fnmatch import*
for x in range(0,10**10,5943):
    if fnmatch(str(x),'73*?859?'):
        print(x,x//5943)
'''

'''def isprime(n):
    for d in range(2,int(n**0.5)+1):
        if x % d == 0:
            return 0
    return 1
from fnmatch import*
for x in range(311,10**8,311):
    if fnmatch(str(x),'17?4*3??') and isprime(x // 311):
        print(x,x//311)'''

'''def isprime(n):
    for d in range(2,int(n**0.5)+1):
        if x % d == 0:
            return 0
    return 1
from fnmatch import*
for x in range(1597,10**8,1597):
    if fnmatch(str(x),'132?5*5??') and isprime(x // 1597):
        print(x,x//1597)'''
