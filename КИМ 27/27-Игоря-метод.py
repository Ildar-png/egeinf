'''from math import *
f = open('27-7-A.txt')
f.readline() #Когда в первой строке есть обозначения столбцов, их нужно вот так пропустить
data = [] #Пустой список для значений
for line in f: #Проходимся по каждой строке
    a = [float(x) for x in line.replace(',', '.').split()] #Из строки получаем список из 2 нецелых чисел, то есть координаты
    data.append(a) #Добавляем координаты в список
print('Кол-во точек - ',len(data)) #Выводим кол-во точек. Удобно, и можно удостовериться в правильности программы на данном этапе

clusters = [] #Пустой список кластеров

while len(data) != 0: #Пока список значений не равен 0...
    clusters.append([data.pop(0)])  #Добавляем значение первой точки в кластер и удаляем его из обзего списка
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p, p1) < 3] #Для выбранной точки ищем соседей, если они ближе определенного значения. Значение расстояния нужно менять так, чтобы кол-во кластеров удовлетворяло условию
        clusters[-1].extend(sosedi) #Добавляем всех соседей в кластер с выбранной точкой
        for p2 in sosedi:
            data.remove(p2) #Удаляем найденных соседей из значений
    print('Точек в кластере - ',len(clusters[-1])) #Выводим кол-во точек в сформированном кластере

def centroid(cl): #Ф-ция, которая принимает на вход кластер и выводит координаты его центроида
    mn = []
    for p in cl:
        sm = sum([dist(p, p1) for p1 in cl if p != p1]) #Для каждой точки в кластере находим сумму расстояний от нее до других
        mn.append([sm, p]) #Добавляем в список сначала сумму расстояний, потом точку, для которой это считалось
    return min(mn)[-1] #Возвращаем точку, для которой сумма расстояний наименьшая

centroids = [centroid(cl) for cl in clusters] #Список центроидов
print('Центроиды - ',centroids) #Выводим их для удобства
#Все, что выше этой строки - шаблон. Подходит и для А, и для В
#Далее находим то, что требуется по заданию
Px = sum(x/len(clusters) for x,y in centroids) * 10000
Py = sum(y/len(clusters) for x,y in centroids) * 10000
print('Ответ A - ',int(Px),int(Py))'''

'''from math import*
f = open('27-8-A.txt')
f.readline()
data = []
for line in f:
    a = [float(x) for x in line.replace(',','.').split()]
    data.append(a)
print('Кол-во точек - ', len(data))

clusters = []

while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p,p1) < 1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ', len(clusters[-1]))

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p1,p) for p1 in cl if p != p1])
        mn.append([sm,p])
    return min(mn)[-1]

centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ',centroids)

Px = sum(x/len(clusters) for x,y in centroids) * 10000
Py = sum(y/len(clusters) for x,y in centroids) * 10000
print('Ответ A - ', int(Px),int(Py))

f = open('27-8-B.txt')
f.readline()
data = []
for line in f:
    a = [float(x) for x in line.replace(',','.').split()]
    data.append(a)
print('Кол-во точек - ', len(data))

clusters = []

while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p,p1) < 1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ', len(clusters[-1]))

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p1,p) for p1 in cl if p != p1])
        mn.append([sm,p])
    return min(mn)[-1]

centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ',centroids)

Px = sum(x/len(clusters) for x,y in centroids) * 10000
Py = sum(y/len(clusters) for x,y in centroids) * 10000
print('Ответ B - ', int(Px),int(Py))'''

'''from math import*
f = open('27-10-A.txt')
f.readline()
data = []
for line in f:
    a = [float(x) for x in line.replace(',','.').split()]
    data.append(a)
print('Кол-во точек - ', len(data))

clusters = []

while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p,p1) < 1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ', len(clusters[-1]))

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p,p1) for p1 in cl if p != p1])
        mn.append([sm,p])
    return min(mn)[-1]

centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ', centroids)

Px = abs(sum([x/len(clusters) for x,y in centroids])) * 10000
Py = abs(sum([y/len(clusters) for x,y in centroids])) * 10000
print('Ответ A - ', int(Px),int(Py))

f = open('27-10-B.txt')
f.readline()
data = []
for line in f:
    a = [float(x) for x in line.replace(',','.').split()]
    data.append(a)
print('Кол-во точек - ', len(data))

clusters = []

while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p,p1) < 1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ', len(clusters[-1]))

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p,p1) for p1 in cl if p != p1])
        mn.append([sm,p])
    return min(mn)[-1]

centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ', centroids)

Px = abs(sum([x/len(clusters) for x,y in centroids])) * 10000
Py = abs(sum([y/len(clusters) for x,y in centroids])) * 10000
print('Ответ B - ', int(Px),int(Py))'''

'''from math import*
f = open('27-11-A.txt')
f.readline()
data = []
for line in f:
    a = [float(x) for x in line.replace(',','.').split()]
    data.append(a)
print('Кол-во точек - ', len(data))

clusters = []
while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p,p1) < 1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ', len(clusters[-1]))

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p,p1) for p1 in cl if p1 != p])
        mn.append([sm,p])
    return min(mn)[-1]

centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ',centroids)

Px = abs(sum([x/len(clusters) for x,y in centroids])) * 10000
Py = abs(sum([y/len(clusters) for x,y in centroids])) * 10000

print('Ответ А - ', int(Px),int(Py))

f = open('27-11-B.txt')
f.readline()
data = []
for line in f:
    a = [float(x) for x in line.replace(',','.').split()]
    data.append(a)
print('Кол-во точек - ', len(data))

clusters = []
while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p,p1) < 0.5]
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ', len(clusters[-1]))

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p,p1) for p1 in cl if p1 != p])
        mn.append([sm,p])
    return min(mn)[-1]

centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ',centroids)

Px = abs(sum([x/len(clusters) for x,y in centroids])) * 10000
Py = abs(sum([y/len(clusters) for x,y in centroids])) * 10000

print('Ответ B - ', int(Px),int(Py))'''

'''from math import*
f = open('27-12-A.txt')
f.readline()
data = []
for line in f:
    a = [float(x) for x in line.replace(',','.').split()]
    data.append(a)
print('Кол-во точек - ', len(data))

clusters = []
while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p,p1) < 1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ',len(clusters[-1]))

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p,p1) for p1 in cl if p != p1])
        mn.append([sm,p])
    return min(mn)[-1]

centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ', centroids)

Px = abs(sum(x/len(clusters) for x,y in centroids)) * 10000
Py = abs(sum(y/len(clusters) for x,y in centroids)) * 10000

print('Ответ A - ', int(Px),int(Py))

f = open('27-12-B.txt')
f.readline()
data = []
for line in f:
    a = [float(x) for x in line.replace(',','.').split()]
    data.append(a)
print('Кол-во точек - ', len(data))

clusters = []
while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p,p1) < 1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ',len(clusters[-1]))

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p,p1) for p1 in cl if p != p1])
        mn.append([sm,p])
    return min(mn)[-1]

centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ', centroids)

Px = abs(sum(x/len(clusters) for x,y in centroids)) * 10000
Py = abs(sum(y/len(clusters) for x,y in centroids)) * 10000

print('Ответ B - ', int(Px),int(Py))'''

from math import*
f = open('27-13-A.txt')
f.readline()
data = []
for line in f:
    a = [float(x) for x in line.replace(',','.').split()]
    data.append(a)
print('Кол-во точек - ', len(data))

clusters = []
while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p1,p) < 1]
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ', len(clusters[-1]))
    if len(clusters[-1]) <= 10:
        clusters.remove(clusters[-1])

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p,p1) for p1 in cl if p1 != p])
        mn.append([sm,p])
    return min(mn)[-1]
centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ',centroids)

Px = abs(sum([x/len(clusters) for x,y in centroids]))
Py = abs(sum([y/len(clusters) for x,y in centroids]))
Ps = sum([len(cluster)/(4*4) for cluster in clusters])
print('Ответ A - ',int((Px + Py)*10000),int(Ps*1000))

f = open('27-13-B.txt')
f.readline()
data = []
for line in f:
    a = [float(x) for x in line.replace(',','.').split()]
    data.append(a)
print('Кол-во точек - ', len(data))

clusters = []
while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p1,p) < 0.5]
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ', len(clusters[-1]))
    if len(clusters[-1]) <= 10:
        clusters.remove(clusters[-1])

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p,p1) for p1 in cl if p1 != p])
        mn.append([sm,p])
    return min(mn)[-1]
centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ',centroids)

Px = abs(sum([x/len(clusters) for x,y in centroids]))
Py = abs(sum([y/len(clusters) for x,y in centroids]))
Ps = sum([len(cluster)/(4*4) for cluster in clusters])
print('Ответ B - ',int((Px + Py)*10000),int(Ps*1000))

