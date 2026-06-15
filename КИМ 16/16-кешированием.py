'''from functools import * #Импорт библиотеки

@lru_cache(None) #Кэширование ф-ции
def f(n): #Ф-ция из условия
    if n <= 5:
        return 1
    return n + f(n - 2)

for i in range(1,2500): #Прогоняем функцию, максимальное значение примерно равно максимальному числу в задаче
    f(i)

print(f(2126)-f(2122))'''

'''from functools import *
@lru_cache(None)
def f(n):
    if n == 0: return 1
    if n == 1: return 3
    if n == 2: return 2
    if n > 2: return f(n-1)*f(n-3)
print(f(7))'''

'''from functools import *
@lru_cache(None)
def f(n):
    if n < 6: return n
    return (3*n-2)*f(n-5)
for i in range(1,20600):
    f(i)
print((f(20568)-51702*f(20563))//f(20553))'''


'''def f(n):
    if n <= 2: return n
    return g(n) + f(n-2)
def g(n):
    if n <= 2: return n
    return f(n-1)-g(n-2)
print(g(15))'''

'''def f(n):
    if n < 3: return 2
    if n > 2 and n % 2 == 0: return 2 * f(n-2) - f(n-1) + 2
    if n > 2 and n % 2 != 0: return 2 * f(n-1) - f(n-2) - 2
print(f(17))
'''

'''def f(n):
    if n <= 10: return n
    if n > 10 and n % 2 == 0: return 2 * f(n-2) + 6
    if n > 10 and n % 2 != 0: return f(n-1) + 2*n
print(f(27)-f(20))
print(3+6+3+8)'''

'''from functools import*
@lru_cache(None)
def f(n):
    if n < 5: return 4**4
    if n > 4: return 4 * f(n-4) + 4
for i in range(1,4500):
    f(i)
print(f(4048)//f(4036))'''

'''def f(n):
    if n <= 10: return n
    if 10 < n <= 36: return n//4 + f(n-10)
    if n > 36: return 2 * f(n-5)
print(f(18))'''

'''from functools import*
@lru_cache(None)
def f(n):
    if n < 3: return 3
    return 2 * n + 5 + f(n-2)
for i in range(1,3050):
    f(i)
print(f(3027)-f(3023))'''

'''def f(n):
    if n > 2000: return 16
    return 2 * f(n+3)
print(f(50)//f(110))
print(1*4*8*5*7*6)'''

'''from functools import*
@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return n * f(n-1)
for i in range(1,2050):
    f(i)
print((f(2024)//4 + f(2023))//f(2022))'''

'''from functools import*
@lru_cache(None)
def f(n):
    if n < 5: return n
    return 2*n * f(n-4)
for i in range(1,14000):
    f(i)
print((f(13766)-9*f(13762))//f(13758))'''

'''def f(n):
    if n < 3: return 1
    if n > 2 and n % 2 == 0: return f(n-1) + n - 1
    if n > 2 and n % 2 != 0: return f(n-2) + 2 * n - 2
print(f(34))'''

'''def f(n):
    if n < 3: return 1
    if n > 2 and n % 2 == 0: return f(n-1) + 2*n - 1
    if n > 2 and n % 2 != 0: return f(n-2) + 2*n
print(f(21) - f(19))'''

'''from functools import*

from sys import*
setrecursionlimit(10000)

@lru_cache(None)
def f(n):
    if n >= 7777: return n
    if n < 7777: return n + 5 + f(n+5)
for i in range(1,2000):
    f(i)
print(f(1101)-f(1111))'''

'''from functools import*
@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return 2 * n * f(n-1) - 1

for i in range(2000):
    f(i)
print(f(2000)/f(1997))'''

'''from functools import*
@lru_cache(None)
def f(n):
    if n >= 2025: return n
    return n//2 + f(n+3)

for i in range(2000):
    f(i)

print(f(2020)-f(2023))'''

'''from functools import*
@lru_cache(None)
def f(n):
    if n <= 10: return n
    return (n+2) * f(n-2)
for i in range(20000):
    f(i)
print((f(12748) - f(19563)) // f(19562) + 1234)'''

'''from functools import*
@lru_cache(5000)
def F(n):
    if n < 11: return 8
    return (n+1)*F(n-5)
for i in range(250000):
    F(i)
print((F(246911) // 8 + 11111 * F(246906)) // F(246901))
'''

'''from functools import*
@lru_cache(None)
def F(n):
    return  2 * (G(n - 3) + 13)
@lru_cache(None)
def G(n):
    if n < 6: return 2*n
    return G(n - 2) + 3
for i in range(15000):
    F(i)
    G(i)
print(F(14541))'''

'''from functools import*
@lru_cache(None)
def F(n):
    if n < 10: return 5
    return (n + 2) * F(n - 5)
for i in range(124000):
    F(i)
print((F(123002) // 7 + 2000 * F(122997)) // F(122992))'''

'''from functools import*
@lru_cache(1000)
def F(n):
    if n >= 29: return  F(n - 7) + 1134
    return 17 * (G(n - 7) - 36)
@lru_cache(30000)
def G(n):
    if n >= 27565: return n / 32 + 33
    return G(n + 13) - 1
for i in range(40000):
    F(i)
    G(i)
print(F(676))'''