'''for a in range(1,10000): # Перебор значений. а можно брать большой, а вот х и у лучше брать поменьше
    a_otw = True # Ввод специальной переменной
    for x in range(1,1000):
        for y in range(1,1000):
            if ((17*x - 3*y + 17 != 0) or (a < x) or (a < y)) == False:
                a_otw = False
                break
        if a_otw == False: # Нужно выходить из двух циклов, проверяя специальную переменную
            break
    if a_otw == True:
        print(a)'''

'''for a in range(1,10000):
    if all((((y + 7*x != 36) or (a > x - 2)) or (a < y + 27)) for x in range(1,1000) for y in range(1,1000)): # Проверка условия, записанная в одну строку с генератором х и у
        print(a)
        break'''

'''for a in range(1,10000):
    a_otw = True
    for x in range(1,1000):
        for y in range(1,1000):
            if (((x >= 17) or (3*x < y)) or (y*x < a)) == False:
                a_otw = False
                break
        if a_otw == False:
            break
    if a_otw == True:
        print(a)
        break'''

'''for a in range(1,10000):
    for x in range(1,1000):
        for y in range(1,1000):
            if ((y - 13*x < a) or (x > 88) or (y > 77)) == False:
                break
        if ((y - 13*x < a) or (x > 88) or (y > 77)) == False: # Можно вместо ввода новой переменной писать еще раз условие выхода из цикла
            break
    else:
        print(a)
        break'''

'''for a in range(0,1000):
    for x in range(0,1000):
        for y in range(0,1000):
            if ((x + 5*y != 29) or ((a > x) and (a > y))) == False:
                break
        if ((x + 5 * y != 29) or ((a > x) and (a > y))) == False:
            break
    else:
        print(a)
        break'''

'''for a in range(0,1000):
    for x in range(1,1000):
        for y in range(1,1000):
            if ((x + 5*y != 29) or ((a > x) and (a > y))) == False:
                break
        if ((x + 5 * y != 29) or ((a > x) and (a > y))) == False:
            break
    else:
        print(a)
        break'''

'''for a in range(0,200000):
    for x in range(1,1000):
        for y in range(1,1000):
            if ((178125 != y + 3*x) or (a > x) and (a > y)) == False:
                break
        if ((178125 != y + 3*x) or (a > x) and (a > y)) == False:
            break
    else:
        print(a)
        break'''

'''for a in range(1,1000000):
    for x in range(1,1000):
        for y in range(1,1000):
            if ((4*y < a) and (2*x < a) or (120000 < 6*y + 2*x)) == False:
                break
        if ((4 * y < a) and (2 * x < a) or (120000 < 6 * y + 2 * x)) == False:
            break
    else:
        print(a)
        break'''

'''for a in range(1,10000):
    if all((((y + 10*x != 28) or (a > x - 1)) and (a < y + 50)) for x in range(0,1000) for y in range(0,1000)):
        print(a)
        break'''

'''for a in range(1,10000):
    if all(((15*x - y + 40 != 0) or (a < x) or (a < y)) for x in range(1,1000) for y in range(1,1000)):
        print(a)'''

'''c = 0
for a in range(0,1000):
    for x in range(0,1000):
        for y in range(0,1000):
            if (((x > 15) <= (x*y + 10*x >= a)) and ((y*x + y > a) <= (y >= 1))) == False:
                break
        if (((x > 15) <= (x*y + 10*x >= a)) and ((y*x + y > a) <= (y >= 1))) == False: # Можно вместо ввода новой переменной писать еще раз условие выхода из цикла
            break
    else:
        c += 1
print(c)'''


