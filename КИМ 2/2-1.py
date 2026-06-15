print('x y z w F') # Первая строка таблицы для удобства
for x in range(2): # Перебор значений
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w <= z) == y) <= x # Ф-ция из условия
                if F == 0: # Значение ф-ции
                    print(x,y,z,w,int(F)) # Вывод в той же последовательности

'''print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or (y and (not z))) and (not w)
                if F == 0:
                    print(x,y,z,w,int(F))'''

'''print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not w) and z and (y <= x)
                if F == 1:
                    print(x,y,z,w,int(F))'''

'''print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = x and (not w) and (y or (not z))
                if F == 1:
                    print(x,y,z,w,int(F))'''

'''print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (x or y) <= (y == z)
            if F == 0:
                print(x,y,z,int(F))'''

'''print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (y or x) <= (z == y)
            if F == 0:
                print(x,y,z,int(F))'''

'''print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not z) and y and x and (not w)) or ((not z) and y and not x and (not w)) or (z and y and x and (not w))
                if F == 1:
                    print(x,y,z,w,int(F))'''

'''print('x y z w F1 F2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 = ((x <= w) == (z <= y))
                F2 = ((x <= w) and ((not y) == z))
                if F1 == 0 and F2 == 1:
                    print(x,y,z,w,int(F1),int(F2))'''

'''print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w <= (not (z <=x))) or y)
                if F == 0:
                    print(x,y,z,w,int(F))'''

'''print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not x) and (z <= y) and (not w)) or ((z == w) and (x or y <= w))
                if F == 1:
                    print(x,y,z,w,int(F))'''

'''print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((z <= x) <= (x == y)) or (not w)
                if F == 0:
                    print(x,y,z,w,int(F))'''