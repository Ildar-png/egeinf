'''from math import * # Импорт библиотеки математика
for n in range(1,10000): # Перебор искомого значения
    N = 1280 * 720 # Переписывание условия
    i = ceil(log2(8192)) # Округленный в меньшую сторону до целого числа двоичный логарифм
    Vn = N * i * n # Объем n-ного кол-ва данных
    t = Vn/1474560 # Время передачи данных
    if t <= 280: # Условие
        print(n)'''

'''from math import *
for n in range(1,10000):
    N = 1920*1080
    i = ceil(log2(16384))
    Vn = N * i * n
    if (Vn/524288) <= 256:
        print(n)'''

'''from math import *
for i in range(1,10000):
    N = 1050*460
    Vn = N*i*64
    if (Vn/1474560)<=200:
        print(2**i)'''

'''from math import *
for i in range(1,10000):
    N = 1024*1024
    Vn = N*i*128
    if (Vn/524288)<=256:
        print(2**i)'''

'''from math import *
for n in range(1,10000):
    N = 1024 * 768
    i = ceil(log2(256))
    V = N * i * n * 0.15
    if (V/(750* 2**13)) <=  1:
        print(n)'''

'''from math import *
for i in range(1,10000):
    V = 2 * i * 48000 * 1 * 0.16
    if (V/(45 * 2**13))<=1:
        print(i)'''

'''a = []
for i in range(1,10000):
    N = 32*1024
    V = 28*1024*8
    P = 2**i
    if N*i<=V:
        a.append(P)
print(max(a))'''

'''for i in range(1,1000):
    N = 2048 * 512
    V = N * i
    A = 2**i
    if V == 2 * 1024 * 1024 * 8:
        print(A)'''

'''for i in range(1,1000):
    N = 1024 * 1024
    V = N * i
    if V <= 1 * 1024 * 1024 * 8:
        print(i)'''

'''from math import*
N = 512 * 256
A = 512
i = ceil(log2(A))
V = (N * i)//(8*1024)
print(V)'''

'''N1 = 4890 * 3570
i1 = 22
V1 = N1 * i1
N2 = 1360 * 1240
i2 = 7
V2 = N2 * i2
O = ((V1-V2)*200)/(8*1024)
print(O)'''

'''nu = 28000
i = 8
t = 2 * 60 + 20
n = 2
V = (nu * t * i * n)/(8*1024)
print(V)
'''

'''n1 = 2
nu1 = 32000
i1 = 32
V1 = 16*1024*1024*8
t = V1/(n1*nu1*i1)
n2 = 1
nu2 = 16000
i2 = 16
V2 = (n2 * nu2 * i2 * t)/(8*1024*1024)
print(V2)'''

'''V = 70/4*4/2
print(V)'''

'''from math import*
A1 = 256
i1 = log2(A1)
N1 = 400*400
V1 = N1 * i1
N2 = 200*200
A2 = 16
i2 = log2(A2)
V2 = N2 * i2
print(520 * (V2/V1))'''

'''N = 768 * 512
V = 640 * 1024 * 8
i = int(V/N - 5)
A = 2**i
print(A)
print(i)
'''

'''N = 64 * 1536
V = 252*1024*8
i = V/N - 7
print(2**i)
'''

'''n = 4
nu = 32000
i = 16
t = 60
V = n * nu * t * i
T = V/2400
print(T)'''

'''N = 2048 * 1536
i = 6 * 8
V = N * i
t = V /131072
print(t)
'''

'''t = 120
n = 2
i = 64
nu = 64000
V = t * n * i * nu
T = 960 * 60
v = V/T
print(v)'''

'''from math import*
N = 1920 * 1920
A = 16384
i = log2(A)
V = N * i
V1 = 1474560 * 280
n = V1 // V
print(n)'''

