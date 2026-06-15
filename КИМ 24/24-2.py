f = open('2.24.8.1_web.txt')
s = f.readline()
cl = 0
ml = 0
for i in range(len(s) - 1):
    if s[i] != s[i+1]: #Если соседние элементы соответствуют условию (разные в данном случае)...
        cl += 1 #Текущая длина увеличивается
        ml = max(ml,cl) #Максимальная длина равна максимуму из уже максимальной и текущей
    else:
        cl = 0 #Иначе текущая длина сбрасывается
print(ml+1) #Первый элемент не считается в программе, поэтому ответом будет максимальная длина, найденная в последовательности, + 1

'''f = open('2.24.8.2_web.txt')
s = f.readline()
cl = 0
ml = 0
for i in range(len(s) - 1):
    if s[i] > '5' and s[i+1] > '5' and int(s[i]) >= int(s[i+1]):
        cl += 1
        ml = max(ml,cl)
    else:
        cl = 0
print(ml + 1)'''

'''f = open('2.24.8.4_web.txt')
s = f.readline()
cl = 0
ml = 0
for i in range(len(s) - 1):
    if s[i].isdigit() and s[i+1].isdigit() and int(s[i]) % 2 != int(s[i+1]) % 2:
        cl += 1
        ml = max(ml,cl)
    else:
        cl = 0
print(ml + 1)
'''