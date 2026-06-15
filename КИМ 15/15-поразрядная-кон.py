'''for a in range(1,1000): #Все как в теор-1, но...
    a_otwet = True
    for x in range(1,1000): #В задании появляется знак поразрядной конъюнкции (&), его просто также пишем в формулу в строке ниже
        if ((x & 79 != 0) <= ((x & 64 == 0) <= (x & a != 0))) == False:
            a_otwet = False
            break
    if a_otwet:
        print(a)
        break'''

#Новая конструкция for else
'''for a in range(1,10000):
    for x in range(1,10000): #Начинаем цикл
        if (((x & 14 != 0) and (x & 61 != 0)) <= ((x & a != 0) and (x & 78 != 0))) == False:
            break #Цикл прервется, когда логическое выражение из условия будет ложью
    else: #Если этого не произошло и цикл не прервался с brake, то выполняется условие записанное в else
        print(a)
        break'''

'''for a in range(1,10000):
    for x in range(1,10000):
        if (((x & 14 != 0) or (x & 64 != 0)) <= ((x & 23 == 0) <= (x & a != 0))) == False:
            break
    else:
        print(a)
        break'''

'''for a in range(1,10000):
    for x in range(1,10000):
        if ((x & 15 != 0) or (x & 34 == 0) or (x & a != 0)) == False:
            break
    else:
        print(a)
        break'''

'''for a in range(1,1000):
    for x in range(1,10000):
        if (((x & 46 == 0) or (x & 18 == 0)) <= ((x & 115 != 0) <= (x & a == 0))) == False:
            break
    else:
        print(a)'''

'''for a in range(1,10000):
    for x in range(1,10000):
        if ((x & 45 != 0) <= ((x & 23 == 0) <= (x & a != 0))) == False:
            break
    else:
        print(a)
        break'''
