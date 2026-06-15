'''from turtle import * # Импорт библиотеки
lt(90)
down()
tracer(0)
screensize(5000,5000)
k = 20 # Коэффициент
# Строки 1 - 6 - шаблон, далее - переписывание условия, менять k для удобства
for i in range(2):
    fd(10*k) # Умножать на k при движении
    rt(90) # Углы поворота не умножать ни на что
    fd(18*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(7*k)
lt(90)
down()
for a in range(2):
    fd(10*k)
    rt(90)
    fd(7*k)
    rt(90)
#Шаблонный цикл рассталения точек
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'red')
done() # Конец
'''
'''from turtle import *
screensize(5000,5000)
tracer(0)
lt(90)
down()
k = 30

for i in range(3):
    fd(2*k)
    rt(90)
    fd(3*k)
    lt(90)
rt(180)
fd(6*k)
rt(90)
fd(9*k)
up()
back(3*k)
rt(90)
down()
for i in range(2):
    fd(1*k)
    rt(90)
    fd(2*k)
    lt(90)
rt(180)
fd(3*k)
rt(90)
fd(4*k)
rt(90)
fd(1*k)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'red')

done()'''

'''from turtle import *
lt(90)
tracer(0)
screensize(5000,5000)
down()
k = 20

lt(180)
for i in range(3):
    rt(45)
    fd(12*k)
    rt(45)
lt(315)
fd(12*k)
for i in range(2):
    rt(90)
    fd(12*k)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'red')
done()'''

'''from turtle import *
down()
lt(90)
tracer(0)
screensize(5000,5000)
k = 20
for i in range(2):
    fd(3*k)
    lt(90)
    back(10*k)
    lt(90)
up()
back(10*k)
rt(90)
fd(8*k)
lt(90)
down()
for i in range(2):
    fd(16*k)
    rt(90)
    fd(8*k)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'red')
done()'''

'''from turtle import*
lt(90)
screensize(5000,5000)
k = 1
speed(0.7)
down()
for i in range(2):
    fd(150*k)
    rt(120)
rt(300)
for i in range(2):
    fd(75*k)
    rt(120)
    fd(75*k)
    lt(120)
rt(180)
for i in range(2):
    fd(150*k)
    rt(120)
lt(60)
fd(75*k)
up()
done()'''

'''from turtle import*
lt(90)
tracer(0)
screensize(5000,5000)
k = 20
rt(45)
for i in range(3):
    rt(45)
    fd(10*k)
    rt(45)
rt(315)
fd(10*k)
rt(90)
fd(20*k)
rt(90)
for i in range(2):
    fd(10*k)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,'red')
done()'''

'''from turtle import*
screensize(5000,5000)
tracer(0)
lt(90)
k = 20

for i in range(2): fd(10*k), lt(270), bk(20*k), rt(90)
up()
fd(15*k), rt(90), bk(7*k), rt(90)
down()
for i in range(2): fd(13*k), rt(90), fd(3*k), rt(90)
up()

for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(3,'red')
done()'''

'''from turtle import*
screensize(5000,5000)
tracer(0)
lt(90)
k = 20

for i in range(2): fd(17*k), lt(90), fd(34*k), lt(90)
up()
fd(10*k), rt(90), fd(15*k), rt(90)
down()
for i in range(2): fd(40*k), rt(90), fd(24*k), rt(90)
up()

for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(3,'red')
done()'''

'''from turtle import*
screensize(5000,5000)
tracer(0)
lt(90)
k = 20

for i in range(4): fd(28*k), rt(90), fd(26*k), rt(90)
up()
fd(8*k), rt(90), fd(7*k), lt(90)
down()
for i in range(4): fd(67*k), rt(90), fd(98*k), rt(90)

up()
for x in range(-20,50):
    for y in range(-20,50):
        goto(x*k,y*k)
        dot(3,'red')
done()
'''

'''from turtle import*
screensize(5000,5000)
tracer(0)
lt(90)
k = 20

for i in range(4): fd(10*k),rt(270)
up()
fd(3*k),rt(270),fd(5*k),rt(90)
down()
for i in range(2): fd(10*k),rt(270),fd(12*k),rt(270)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(3,'red')
done()'''

from turtle import*
screensize(5000,5000)
tracer(0)
lt(90)
k = 20

for i in range(2): fd(24*k), rt(90),fd(20*k),rt(90)
up()
fd(7*k),rt(90),fd(7*k),lt(90)
down()
for i in range(2): fd(60*k),rt(90),fd(100*k),rt(90)

up()
for x in range(-20,50):
    for y in range(-20,50):
        goto(x*k,y*k)
        dot(3,'red')
done()