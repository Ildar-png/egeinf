'''def f(n): # Создание ф-ции
    if n < 2: # Условие
        return 1
    return f(n-1)*(n+5) # Другое условие
print(f(2))
'''
'''def f(n):
    if n == 1:
        return 3
    return 4 * f(n-1) - 3 * n
print(f(5))'''

'''def f(n):
    if n > 15:
        return n * 2
    return 2 * f(n + 2) + 4 * n
print(f(7))'''

'''def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return f(n-1) + 7
    else:
        return f(n-2) + 4 * n
print(f(100))
'''

'''def f(n):
    if n <= 4:
        return 0
    if n > 4 and n % 4 == 0:
        return f(n-1) + 3 * n
    else:
        return f(n-(n%4)) + 8 * n - 2
print(f(43))'''

'''def f(n):
    if n == 2:
        return 1
    if n > 2 :
        return 3*f(n - 1) + 4*g(n - 1) - n*2 + 4


def g(n):
    if n == 2 :
        return 1
    if n > 2:
        return 4*f(n-1)+3*g(n-1)+6

print(f(8)+g(8))'''

'''def f(n):
    if n == 1:
        return 1
    if n > 1 :
        return g(n - 1) + 3*f(n - 1) - n*5 + 1'''

'''def g(n):
    if n == 1 :
        return 1
    if n > 1:
        return 2*f(n-1)-g(n-1)+4*n-2

print(g(12))'''

'''from sys import*
setrecursionlimit(5000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1)
print((f(2024) - 2 * f(2023))//f(2022))'''

'''def f(n):
    if n == 1:
        return 2
    if n > 1:
        return f(n-1)+3
print(f(3))'''

'''def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)*2
print(f(4))'''

'''def f(n):
    if n == 0:
        return 5
    if n > 0:
        return f(n-1)+2
print(f(2))'''

'''def f(n):
    if n == 1:
        return 3
    if n > 1:
        return f(n-1)+(n-1)*n
print(f(18))'''

'''def f(n):
    if n == 1:
        return 2
    if n > 1:
        return 4* f(n-1) + 2*n
print(f(8))'''

'''def f(n):
    if n < 4 :
        return 4 * n - 1
    if n % 2 == 0:
        return f(n - 2) + 2 * n
    else:
        return f(n-4) + 4*n + 5
print(f(62))'''

'''def f(n):
    if n == 0  :
        return 0
    if n > 0 and n % 3 == 0:
        return f(n - 1) + 3 * n
    if n > 0 and n % 3 > 0:
        return f(n - (n % 3)) + 8 * n - 2
print(f(30))'''

'''def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (3 * f(n - 1) - g(n - 1)) * 2

def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) - 3 * g(n - 1) + 1
print(f(7))'''

'''def f(n):
    if n > 10  :
        return n
    if n <= 10:
        return 2 * f(n + 1) + 2 * n
print(f(4))'''

'''def f(n):
    if n == 1  :
        return 4
    if n > 1:
        return 5 * f(n - 1) - 2 * n
print(f(6))'''

'''def f(n):
    if n == 1: return 2
    if n > 1: return 4*f(n-1)+2*n
print(f(8))'''

'''def f(n):
    if n == 2: return 2
    if n > 2 and n % 2 == 0: return f(n-1) + 3
    if n > 2 and n % 2 != 0: return f(n-3) + 2*n
print(f(30))'''

'''def F(n):
    if n == 1: return 1
    if n>1: return F(n - 1) + 15 * G(n - 1) + 2*n
def G(n):
    if n == 1: return 1
    if n > 1: return F(n - 1) - 8 * G(n - 1)
print(F(10) * G(2))'''

'''def F(n):
    if n >= 2023: return n
    return n // 3 + F(n + 2)
print(F(2015) - F(2018))'''