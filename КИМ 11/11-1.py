'''from math import * # Импорт библиотеки математика
for N in range(1,10000): # Перебор искомого значения
    A = 10 + 52 + 1000 # Алфавит, состоящий из разных символов
    i = ceil(log2(A)) # Вес одного символа через целую степень двойки
    V1 = ceil((N * i)/8) # Объем 1 штуки в байтах
    V777 = (777 * V1)/1024 # Объем n штук
    if V777 <= 276: # Условие
        print(N) # Ответ
'''
'''for N in range(1,10000):
    A = 10 + 26 + 232
    i = ceil(log2(A))
    V1 = ceil((N * i) / 8)
    V760 = (V1 * 760) / 1024
    if V760 > 140:
        print(N)
        break'''

'''for A in range(1,10000):
    N = 191
    i = ceil(log2(A))
    V1 = ceil((N*i)/8)
    V = (V1 *131072)/(2**20)
    if V > 22:
        print(A)'''

'''for A in range(1,10000):
    N = 205
    i = ceil(log2(A))
    V1 = ceil((N*i)/8)
    V = (V1 * 8192)/1024
    if V <= 899:
        print(A)'''

'''for N in range(1,10000):
    A = 10 + 52 + 980
    i = ceil(log2(A))
    V1 = ceil((N*i)/8)
    V = (V1 * 385)/1024
    if V < 136:
        print(N)'''

'''for N in range(1,10000):
    A = 10 + 52 + 5000
    i = ceil(log2(A))
    V1 = (N*i)/8
    V = (V1*949)/1024
    if V > 727:
        print(N)
        break'''

'''for A in range(1,100000):
    N = 283
    i = ceil(log2(A))
    V1 = ceil((N*i)/8)
    V = (65536*V1)/(2**20)
    if V > 15:
        print(A)
        break'''
'''from math import *
n = 200
A = 10 + 2040
i = ceil(log2(A))
V = ceil((n * i)/8)
V1 = ceil((V * 98304)/1024)
print(V1)'''

'''from math import*
for N in range(1,10000):
    A = 10 + 26 + 34
    i = ceil(log2(A))
    V = ceil((N * i)/8)
    V1 = V * 1142
    if V1 >= 305 * 1024:
        print(N)
        break
print(int('1000100000',2))'''

'''from math import*
N = 20
A = 11*2 + 10
i = ceil(log2(A))
V = ceil((N*i)/8)
print(V*60)'''

'''from math import*
N = 400
A = 10 + 4090
i = ceil(log2(A))
V = ceil((N*i)/8)
V1 = (V * 16384)/1024
print(V1)'''

'''from math import*
N = 12
A = 26*2 + 6 + 10
i = ceil(log2(A))
V = ceil((N*i)/8)
V1 = 1080/40
print(V1-V)'''

'''from math import*
N = 19
A = 10
i = ceil(log2(A))
V = ceil((N*i)/8)
Vi = 43
V1 = V + Vi
print(V1*60)'''

'''from math import*
for n in range(1,1000):
    N = 23
    A = 65*2 + 10
    i = ceil(log2(A))
    V = ceil((N*i)/8)
    Vi = 49
    V1 = V + Vi
    if V1 * n <= 4 * 1024:
        print(n)'''

'''from math import*
for N in range(1,1000):
    A = 10 + 52 + 4044
    i = ceil(log2(A))
    V = ceil((N*i)/8)
    if (V * 7777) <= (566 * 1024):
        print(N)'''

'''from math import*
for i in range(1,1000):
    N = 256
    V = ceil((N*i)/8)
    if V * 32768 > 8 * 1024 * 1024:
        print(2**(i-1)+1)
        break'''

'''from math import*
for N in range(1,1000):
    A = 10 + 52 + 980
    i = ceil(log2(A))
    V = ceil((N*i)/8)
    if V * 385 < 136 * 1024:
        print(N)'''

'''from math import*
N = 840*110
A = 2543
i = ceil(log2(A))
V = N * i
Vp = 1459960*237*2
Vd = (Vp % V)/8
print(Vd)'''

from math import*
Nn = 15
An = 26*2 + 10
In = ceil(log2(An))
Vn = ceil((Nn*In)/8)
Np = 20
Ap = 26*2 + 33*2 + 10 + 8
Ip = ceil(log2(Ap))
Vp = ceil((Np*Ip)/8)
No = 100
Vo = ceil((No*Ip)/8)
print(Vn+Vp+Vo)

