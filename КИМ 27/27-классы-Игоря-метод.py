#Код отличается от предыдущего в паре мест
from math import*
from fnmatch import* #Классы звезд лучше определять с помощью fnmatch
f = open('1_27_A.txt')
f.readline()
data = []
for line in f:
    x,y,type = [x for x in line.replace(',','.').split()]
    x,y = float(x),float(y)
    data.append([[x,y],type]) #Теперь список data содержит 2 элемента: координату(x,y) и тип
print('Кол-во точек - ',len(data))

clusters = []
while len(data) != 0:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p[0],p1[0]) < 1] #Теперь везде, где фигурируют точки, нужно брать 0-ой элемент
        clusters[-1].extend(sosedi)
        for p2 in sosedi:
            data.remove(p2)
    print('Точек в кластере - ',len(clusters[-1]))
    if len(clusters[-1]) < 10:
        clusters.remove(clusters[-1])

def centroid(cl):
    mn = []
    for p in cl:
        sm = sum([dist(p[0],p1[0]) for p1 in cl if p != p1])
        mn.append([sm,p])
    return min(mn)[-1]
centroids = [centroid(cl) for cl in clusters]
print('Центроиды - ',centroids)
#Далее идет поиск нужных по заданию значений
mn = []
for p in clusters[0]:
    if fnmatch(p[-1],'M?III'): #Вот так с помощью fnmatch можно определить тип звезды
        sm = sum([dist(p[0], centroids[0][0]) for p1 in clusters[0] if p != p1])
        mn.append([sm, p])
Ax = min(mn)[-1][0][0]
Ay = min(mn)[-1][0][1]
print('Ответ А -',int(abs(Ax*10000)),int(abs(Ay*10000)))