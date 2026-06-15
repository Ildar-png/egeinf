p = list(range(3,19)) # Задаем отрезки из условия, помни, что конец пишется не включительно, значит нужно писать на 1 больше
q = list(range(11,25))
a = [] # Создаем пустой "отрезок"
for x in range(1,100): # Перебираем а
    if (((x in p) and (x in q)) <= (x in a)) == False: # Если условие не выполняется...
        a.append(x) # Добавляем значение на отрезок
print(a) # Итоговый полученный отрезок в форме списка с входящими туда значениями
print(max(a) - min(a)) # Длина отрезка, это максимальное минус минимальное

'''p = list(range(16,60))
q = list(range(27,72))
a = []
for x in range(1,1000):
    if ((not(x in a)) <= ((x in p) <= (not(x in q)))) == False:
        a.append(x)
print(a)
print(max(a)-min(a))'''

'''p =list(range(13,34))
q =list(range(22,46))
a = []
for x in range(1,100):
    if ((not(x in a)) <= (((x in p) and (x in q)) <= (x in a))) == False:
        a.append(x)
print(a)
print(max(a) - min(a))'''

'''p =list(range(11,29))
q =list(range(21,42))
a = list(range(1,100)) # Нужен наибольший а, поэтому берем заполненный список, вместо пустого
for x in range(1,100):
    if (((x in p) <= (x in q)) <= (not(x in a))) == False:
        a.remove(x) # А здесь убираем значения, вместо того, чтобы добавлять
print(a) 
print(21 - 11) # Отрезок выбирается среди данных в условии чисел, тут мин - 11, макс - 20, но 20 нет, значит ответ 21 - 11 = 10
'''

'''p = list(range(13,33))
q = list(range(15,20))
a = list(range(1,100))
for x in range(1,100):
    if (((x in a) <= (x in p)) or (x in q)) == False:
        a.remove(x)
print(a)
print(32 - 13)'''

'''b = list(range(22,41))
c = list(range(32,51))
a = []
for x in range(1,1000):
    F = (not (x in a)) <= ((x in b) == (x in c))
    if F == 0:
        a.append(x)
print(max(a)-min(a))'''

'''q = list(range(17,91))
p = list(range(10,47))
a = []
for x in range(1,100):
    if (((x in p) and (x in q)) <= (x in a)) == False:
        a.append(x)
print(a)
print(47-17)'''

'''q = list(range(12,30))
p = list(range(5,42))
a = []
for x in range(1,100):
    if (((x in a) and (x in p)) or (not(x in q))) == False:
        a.append(x)
print(a)
print(29-12)'''

'''q = list(range(8,17))
p = list(range(12,29))
a = list(range(1,100))
for x in range(1,100):
    if ((x in a) <= ((x in p) and (not(x in q))) )== False:
        a.remove(x)
print(a)
print(28-16)'''

'''q = list(range(12,23))
p = list(range(3,13))
a = list(range(1,100))
for x in range(1,100):
    if (((x in a) <= (x in p)) or (x in q)) == False:
        a.remove(x)
print(a)
print(22-3)'''

'''q = list(range(37,84))
p = list(range(17,55))
a = []
for x in range(1,100):
    if (((x in p) and (x in q)) <= (x in a)) == False:
        a.append(x)
print(a)
print(54-37)'''

'''q = list(range(10,56))
p = list(range(4,20))
a = []
for x in range(1,100):
    if ((x in a) or ((not(x in p)) <= (not x in q))) == False:
        a.append(x)
print(a)
print(55-20)'''

'''q = list(range(33,88))
p = list(range(10,49))
a = list(range(1,100))
for x in range(1,100):
    if (((x in p) <= (not(x in q))) <= (not(x in a))) == False:
        a.remove(x)
print(a)
print(49-33)'''

'''q = list(range(18,33))
p = list(range(5,21))
a = list(range(1,100))
for x in range(1,100):
    if (((x in a) <= (x in p)) or (x in q)) == False:
        a.remove(x)
print(a)
print(32-5)'''

