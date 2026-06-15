f = open('26.9a714cf2-7124-494b-a941-dffcf9e0497f_26.2.txt')
n = int(f.readline())
data = [[]for _ in range(100001)] #Создаем список списков, там храним информацию о каждом месте каждого ряда
res = [] #Список для ответа
for s in f:
    row, place = map(int,s.split()) #Считываем ряд и место
    if place not in data[row]: #Если значение не является дубликатом...
        data[row].append(place) #Добавляем его
for row in range(100001): #Проходимся по всем рядам
    if len(data[row]) == 0: #Если точек в ряду нет вообще...
        continue #Скип
    data[row] = sorted([-10000] + data[row] + [200000]) #В начало и конец списка добавляем большие числа, чтобы сравнивать было удобнее
    isolated = 0
    for j in range(1, len(data[row]) -1):
        if (data[row][j] - data[row][j - 1]) > 1000 and (data[row][j + 1] - data[row][j]) > 1000: #Если у точки расстояние до соседей больше 500...
            isolated += 1 #Изолированных точек на одну больше
    res.append([isolated,row]) #Добавляем кол-во изолированных и ряд в список
res.sort(reverse=True)
print(res[:10]) #Лучше выводить 10 последних значений, чтобы убедиться в правильности ответа