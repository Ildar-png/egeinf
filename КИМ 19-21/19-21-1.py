def f(s,m): # Создание ф-ции
    if s<=12: # Условие конца игры
        return m%2==0 # Вывод значения
    if m==0: # Если ходы кончились
        return 0
    h = [f(s-12,m-1),f(s//3,m-1)] # Список с ходами f(s+(действие игрока),m-1 ходы заканчиваются)
    return any(h) if m % 2 !=0 else all(h) # Хз как это работает
print('19 - ',[s for s in range(13,1300) if not f(s,1) and f(s,2)]) # S дано по условию, либо просто надо поставить большое, а дальше условия выигрыша по ходам в игре (Петя - четные, Ваня - нечетные)
print('20 - ',[s for s in range(13,1300) if not f(s,1) and f(s,3)]) #Переписать номер задания и условия в конце строчки
print('21 - ',len([s for s in range(13,1300) if not f(s,2) and f(s,4)]))

'''def f(s,m):
    if s >= 301:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s+3,m-1),f(s*5,m-1)]
    return any(h) if m%2!=0 else all(h)
print('19 - ',[s for s in range(1,301) if not f(s,1) and f(s,2)])
print('20 - ',[s for s in range(1,301) if not f(s,1) and f(s,3)])
print('21 - ',[s for s in range(1,301) if not f(s,2) and f(s,4)])'''

