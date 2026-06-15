'''def f(s,e): # Создание ф-ции
    if s > e or s == 30: # Условия для остановки (перелет конца и число, которое не ложно входить в путь вычислений по условию)
        return 0
    if s == e: # Проверка на возможность работы такой программы
        return 1
    return f(s+1,e) + f(s*3,e) # Сумма путей
print(f(3,20)*f(20,120)) # Точка z , обязательно входящая в путь от x до y встраивается так f(x,z)*f(z,y)
'''
'''def f(s,e):
    if s < e or s == 48:
        return 0
    if s == e:
        return 1
    return f(s-1,e) + f(s//2,e) + f(s//3,e)
def d(s,e):
    if s < e or s == 61:
        return 0
    if s == e:
        return 1
    return d(s-1,e) + d(s//2,e) + d(s//3,e)
print(f(106,61)*f(61,6) + d(106,48)*d(48,6))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*2,e)
print(f(2,4))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*2,e)
print(f(1,5))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*2,e)
print(f(1,16))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*3,e)+f(s**2,e)
print(f(3,77))'''

'''def f(s,e):
    if s > e or s == 30:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*3,e)
print(f(3,20)*f(20,80))'''

'''def f(s,e):
    if s > e or s == 19:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*2,e)
print(f(2,10)*f(10,29))'''

'''def f(s,e):
    if s < e:
        return 0
    if s == e:
        return 1
    return f(s-1,e)+f(s//3,e)
print(f(33,7)*f(7,2))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s+10,e)
print(f(12,27))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*2,e)+f(s*2+1,e)
print(f(1,24))'''

'''def f(s,e):
    if s > e or s == 50:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*4,e)
print(f(1,12)*f(12,118))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*2,e)
print(f(1,14))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*3,e)
print(f(2,56))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*3,e)+f(s**2,e)
print(f(4,93))'''

'''def f(s,e):
    if s > e or s == 27:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*2,e)
print(f(3,15)*f(15,72))'''

'''def f(s,e):
    if s > e or s == 44:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*3,e)
print(f(2,24)*f(24,144))'''

'''def f(s,e):
    if s < e:
        return 0
    if s == e:
        return 1
    return f(s-1,e)+f(s//3,e)
print(f(49,11)*f(11,1))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s+10,e)
print(f(2,45))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+2,e)+f(s*2,e)+f(s*2+1,e)
print(f(3,90))'''

'''def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*10+1,e)
print(f(1,928))'''

'''def f(s,e):
    if s > e or s == 14:
        return 0
    if s == e:
        return 1
    return f(s+1,e)+f(s*2,e)+f(s*3,e)
print(f(2,39))'''

'''def f(s,e):
    if s < e:
        return 0
    if s == e:
        return 1
    return f(s-1,e) + f(s//2, e)
print(f(40,7)*f(7,6))'''

'''def f(s,e):
    if s < e or s == 28:
        return 0
    if s == e:
        return 1
    return f(s-3,e) + f(s//3,e) + f(s//2,e)
print(f(46,20)*f(20,3))'''

'''def f(s,e):
    if s > e: return 0
    if s == e: return 1
    return f(s+2,e) + f(s*3,e)
print(f(1,15))'''

'''def f(s,e):
    if s > e or s == 15: return 0
    if s == e: return 1
    return f(s+1,e) + f(s+2,e) + f(s*2,e)
print(f(4,34))'''

'''def f(s,e):
    if s > e or s == 21: return 0
    if s == e: return 1
    return f(s+3,e) + f(s*3,e)
print(f(1,10)*f(10,72))'''

'''def f(s,e):
    if s < e: return 0
    if s == e: return 1
    return f(s-1,e) + f(s // 3,e)
print(f(37,7)*f(7,2))'''

'''def f(s,e):
    if s > e or s == 15 or s == 23: return 0
    if s == e: return 1
    return f(s+2,e) + f(s*2,e) + f(s*3,e)
print(f(3,11)*f(11,48)+f(3,18)*f(18,48))'''

'''def f(s,e):
    if s > e: return 0
    if s == e: return 1
    return f(s+2,e) + f(s*2,e) + f(s+3,e) + f(s*3,e)
print(f(1,51))'''

'''def t(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s % 100 // 10 < s % 10:
        return t(s + 1, e) + t(int(str(s)[0] + str(s)[2] + str(s)[1]), e)
    return t(s + 1, e)
print(t(106, 163))'''

'''def task23(start, end, k):
    if start > end or (start == end and k < 2):
        return 0
    if start == end:
        return 1
    if k >= 2:
        return task23(start + 2, end, k) + task23(start + 3, end, k)
    if k < 2:
        return task23(start + 2, end, k) + task23(start + 3, end, k) + task23(start * 2, end, k + 1) + task23(start * 3, end, k + 1)
print(task23(1, 51, 0))'''