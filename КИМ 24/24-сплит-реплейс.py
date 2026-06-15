'''f = open('24_2_дз.txt') #Кидаем файл в переменную
s = f.readline() #Преобразовываем файл в строку для дальнейшей работы
s = s.replace('YYZX', 'YYZ YZX') #В искомой строке не должно быть YYZX, поэтому каждую такую последовательность разбиваем разбиваем на YYZ и YZX
a = s.split() #В новую переменную записываем файл s, разбивая его на отдельные элементы списка по пробелу, также можно указать другой элемент по которому будет деление
print(len(max(a, key = len))) #Ответ - длина максимального по длине элемента списка a
#В функции max можно указать критерий, по которому будет выбираться элемент. В данной задаче key = len - выбирается максимальный по длине элемент
'''

'''f = open('24_7_дз.txt') #Записываем файл в переменную
s = f.readline() #Читаем строки и записываем их в переменную
for i in range(1000): 
    if 'B'*i in s: #Есть ли i-ное кол-во символа в s
        print(i)'''

'''f = open('24_2_dz_VGAwlKK.txt')
s = f.readline()
a = s.split('Y')
print(len(max(a, key = len)))
'''
'''f = open('24_22_дз.txt')
s = f.readline()
s = s.replace('YYZX','YYZ YZX')
a = s.split()
print(len(max(a,key = len)))'''

'''f = open('24_4_§І.txt')
s = f.readline()
s = s.replace('ZXY','*')
s = s.replace('ZYX','*')
for i in range(1,1000):
    if '*'*i in s:
        print(i)'''

'''f = open('24.5555.txt')
s = f.readline()
s = s.replace('E','A')
s = s.replace('M','B')
s = s.replace('I','A')
s = s.replace('K','B')
s = s.replace('O','A')
for i in range(1000):
    if 'BA'*i in s:
        print(i)'''

f = open('24.6.txt')
s = f.readline()
s = s.replace('ANT','AN NT')
s = s.replace('AN','NT')
for i in range(1000):
    if 'NT'*i in s:
        print(i)