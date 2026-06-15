f = open()
s = f.readline()
buff = s[0]
numbers = []
for i in range(len(s)-1):
    if s[i].isdigit() and s[i+1].isdigit():
        buff += s[i+1]
    else:
        buff = s[i+1]
    if buff.isdigit() and int(buff) % 2 != 0:
        numbers.append(int(buff))
print(max(numbers))

'''f = open()
s = f.readline()
buff = s[0]
numbers = []
for i in range(len(s) - 1):
    if int(s[i]) + int(s[i+1]) >= 10:
        buff += s[i+1]
    else:
        buff = s[i+1]
    numbers.append(buff)
print(len(max(numbers, key = len)))'''

'''f = open()
s = f.readline()
alph = 'GHIJKLMNOPQRSTUVWXYZ'
for symb in alph:
    s = s.replace(symb,' ')
a = s.split
print(len(max(a,key = len)))'''

'''from string import hexdigits
f = open()
s = f.readline()
buff = s[0]
numbers = []
for i in range(len(s)-1):
    if s[i] in hexdigits and s[i+1] in hexdigits:
        buff += s[i+1]
    else:
        buff = s[i+1]
    numbers.append(buff)
print(len(max(numbers, key = len)))'''

#0000000000000000000000000000
'''f = open('_24_5.txt')
s = f.readline()
for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    s = s.replace(i,' ')
a = s.split(' ')
mini = 999999
for i in range(len(a)):
    if len(a[i]) == 6 and a[i][0] != '0':
        mini = min(mini,int(a[i]))
print(mini)'''

'''f = open('_24_222.txt')
s = f.readline()
for i in 'QWERTYUIOPASDFGHJKLZXCVBNM24680':
    s = s.replace(i,' ')
a = s.split(' ')
maxi = 0
for i in range(len(a)):
    if len(a[i]) > 0:
        maxi = max(maxi,int(a[i]))
print(maxi)'''

'''f = open('_24.333333 (1).txt')
s = f.readline()
for i in 'HIJKLMNOPQRSTUVWXYZ':
    s = s.replace(i,' ')
a = s.split(' ')
print(len(max(a,key = len)))'''

'''def sm(n):
    s = 0
    for i in str(n):
        s += int(i)**len(str(n))
    return s

f = open('_24.44444.txt')
s = f.readline()
numb = 0
for i in range(len(s)-5):
    for z in range(1,6):
        if int(s[i:i+z]) == sm(s[i:i+z]):
            numb = max(numb,int(s[i:i+z]))
print(numb)
print(s.count(str(numb)))'''

'''def sist(n):
    c = []
    for i in str(n):
        c.append(int(i,35))
    return max(c) + 1

f = open('_24_55555.txt')
s = f.read().splitlines()
a = 0
for i in range(len(s)):
    if s[i][0] != '0' and sist(s[i]) <= 14 and int(s[i],sist(s[i])) % 15 == 0:
        a += 1
print(a)'''








