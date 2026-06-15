def f(s1,s2,m): #Две кучи
    if s1 + s2 >= 211: #Условие выигрыша
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1+1,s2,m-1), f(s1*2,s2,m-1),f(s1,s2+1,m-1), f(s1,s2*2,m-1)] #Список ходов для 2 куч
    return any(h) if m % 2 != 0 else all(h) #Если ход НЕУДАЧНЫЙ all меняется на any в рамках одного номера
print('19 - ', [s for s in range(2,194) if not f(17,s,1) and f(17,s,2)])
print('20 - ', [s for s in range(2,194) if not f(17,s,1) and f(17,s,3)])
print('21 - ', [s for s in range(2,194) if not f(17,s,2) and f(17,s,4)])

'''def f(s1,s2,m):
    if s1 + s2 >= 207:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1+1,s2,m-1),f(s1,s2+1,m-1),f(s1*2,s2,m-1),f(s1,s2*2,m-1)]
    return any(h) if m % 2 != 0 else all(h)
print('19 - ', [s2 for s2 in range(2,190) if not f(17,s2,1) and f(17,s2,2)])
print('20 - ', [s2 for s2 in range(2,190) if not f(17,s2,1) and f(17,s2,3)])
print('21 - ', [s2 for s2 in range(2,190) if not f(17,s2,2) and f(17,s2,4)])'''

'''def f(s1,s2,m):
    if s1 + s2 >= 154:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1+4,s2,m-1),f(s1,s2+4,m-1),f(s1*3,s2,m-1),f(s1,s2*3,m-1)]
    return any(h) if m % 2 != 0 else all(h)
print('19 - ', [s2 for s2 in range(1,143) if not f(11,s2,1) and f(11,s2,2)])
print('20 - ', [s2 for s2 in range(1,143) if not f(11,s2,1) and f(11,s2,3)])
print('21 - ', [s2 for s2 in range(1,143) if not f(11,s2,2) and f(11,s2,4)])'''