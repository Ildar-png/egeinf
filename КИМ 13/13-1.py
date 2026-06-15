'''from ipaddress import*
print(2**12 - 2)'''

from ipaddress import* # Импорт библиотеки
net = ip_network('192.168.32.64/255.255.255.192',0) # Переписываем условие. Функция нетворк принимает адрес сети/узла и маску и создает сеть в которой есть маска, адрес сети и адреса всех входящих в нее узлов
c = 0 # Счетчик
for ip in net: # Перебираем то, что выдал нетворк
    if str(f'{ip:b}')[-3:] == '101': # Проверка условия задачи
        c += 1
print(c)

'''from ipaddress import *
c = [] # Вводим пустой список для подходящих масок
for m in range (33): # Маска может быть представлена числом единиц в ней от 0 до 32. Перебираем маски
    net = ip_network(f'175.184.52.103/{m}',0)
    if str(net.network_address) == '175.184.48.0': # Если адрес сети совпадает с данным по условию, значит маска подходит
        c.append(m) # Записываем в список подходящую маску
print(max(c)) # Т.к маски в задании представлены кол-вом единиц, просто выводим максимальное число из списка подходящих масок'''

'''from ipaddress import*
c = 0
net = ip_network('192.168.32.48/255.255.255.192',0) # Создаем сеть
for ip in net:
    if f'{ip:b}'.count('1') % 5 != 0: # Если кол-во единиц в двоичной записи айпи адреса не кратно 5...
        c += 1 # Счётчик +1
print(c)'''

'''from ipaddress import*
a = []
net = ip_network('98.71.254.171/255.248.0.0',0)
for ip in net:
    if f'{ip:b}'.count('1') % 5 == 0: # Если кол-во единиц в двоичной записи айпи адреса кратно 5...
        a.append(ip) # Добавляем подходящий в список
print(max(a)) # Выводим максимальный'''

'''from ipaddress import*
a = []
net = ip_network('192.168.12.207/255.192.0.0',0)
for ip in net:
    if f'{ip:b}'.count('1') == 16: # Если кол-во единиц в двоичн записи алреса равно кол-ву нулей, значит кол-во одного и другого будет 16
        a.append(ip)
print(max(a))'''

'''from ipaddress import*
a = []
for m in range(33):
    net = ip_network(f'168.224.22.193/{m}',0)
    if str(net.network_address) == '168.224.16.0':
        a.append(m)
print(min(a))'''

'''from ipaddress import *
c = [] # Пустой список для подходящих значений 
s = [int('00000000',2),int('10000000',2),int('11000000',2),int('11100000',2),int('11110000',2),int('11111000',2),int('11111100',2),int('11111110',2),int('11111111',2)] # Список всех значений, которые могут быть на месте а в маске в десятичном виде
for a in s:
    net = ip_network(f'187.124.21.237/255.255.{a}.0',0)
    for ip in net:
        if f'{ip:b}'[:16].count('1') < f'{ip:b}'[16:].count('1'): # Если есть адрес, который выполняет условие ОБРАТНОЕ данному в задаче...
            break # Цикл прерывается, значение а неправильное, выходим из цикла, проверяем другое
    else: # Если все адресы соответствуют условию задачи...
        c.append(a) # Число а подходит, записываем в список подходящих
print(min(c))'''

'''from ipaddress import *
net = ip_network('5.2.5.0/255.255.0.0',0)
c = 0
for ip in net:
    if f'{ip:b}'.count('0') % 25 == 0:
        c += 1
print(c)'''

'''from ipaddress import *
a = []
net = ip_network('205.99.68.249/255.255.248.0',0)
for ip in net.hosts():
    a.append(ip)
print(max(a))'''

'''from ipaddress import *
net = ip_network('98.71.254.171/255.248.0.0',0)
for ip in net.hosts():
    if f'{ip:b}'.count('1') % 7 == 0:
        print(ip)
        break'''

'''from ipaddress import *
net = ip_network('158.214.121.40/255.255.255.224',0)
for ip in net.hosts():
    print(ip)
    break'''

'''from ipaddress import *
c = 0
for m in range(33):
    net = ip_network(f'133.57.64.130/{m}',0)
    if str(net.network_address) == '133.57.64.0':
        c += 1
print(c)'''

'''from ipaddress import *
c = 0
net = ip_network('95.24.20.25/255.255.252.0',0)
for ip in net.hosts():
    c +=1
print(c-1-3-4-2-1)'''

'''from ipaddress import *
c = 0
net = ip_network('172.16.80.0/255.255.248.0',0)
for ip in net:
    if f'{ip:b}'.count('1') % 2 != 0:
        c += 1
print(c)'''

'''from ipaddress import *
c = 0
net = ip_network('172.16.96.0/255.255.224.0',0)
for ip in net:
    if f'{ip:b}'.count('1') % 2 == 0:
        c += 1
print(c)'''

'''from ipaddress import*
net = ip_network('68.203.243.87/255.255.224.0',0)
for ip in net.hosts():
    print(ip)'''

'''from ipaddress import*
for A in range(0,256):
    net = ip_network(f'32.0.{A}.5/255.255.240.0',0)
    for ip in net:
        if (f'{ip:b}'[:16].count('1') <= f'{ip:b}'[16:].count('1')) == False:
            break
    else:
        print(A)'''
