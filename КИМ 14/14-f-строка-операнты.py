for x in '0123456789abc': # Значения, которые может принимать х в зависимости от системы счисления
   if (int(f'9{x}ab',13) + int(f'{x}46c',16) - int(f'b7{x}',15))%14==0: # х вставлен внутрь числа ввиде цифры с помощью f'{x}'
       print(x, (int(f'9{x}ab',13) + int(f'{x}46c',16) - int(f'b7{x}',15))/14) #Вывод х и остаток деления выражения на число по условию

'''for x in '0123456789abcdefghijkl':
    if (int(f'56{x}c20', 22) + int(f'89f{x}2', 22) + int(f'h24{x}k21',22)) % 21 == 0:
        print(x, (int(f'56{x}c20', 22) + int(f'89f{x}2', 22) + int(f'h24{x}k21',22)) / 21)'''

'''for x in '0123456789abc':
    if (int(f'753{x}2',13) + int(f'2{x}173', 13)) % 12 == 0:
        print(x, (int(f'753{x}2',13) + int(f'2{x}173', 13)) / 12)'''

'''for x in '0123456789abcdefghi':
    if (int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)) % 18 == 0:
        print(x, (int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)) / 18)'''

'''for x in '0123456789abcdefg':
    if (int(f'12346{x}17', 17) + int(f'7{x}171', 17)) % 16 == 0:
        print(x, (int(f'12346{x}17', 17) + int(f'7{x}171', 17)) / 16)'''

'''for x in '0123456789abcdefgh':
    if (int(f'ab5{x}3', 18) + int(f'ef{x}13',18)) % 17 == 0:
        print((int(f'ab5{x}3', 18) + int(f'ef{x}13',18)) // 17)'''

'''for x in '0123456789ABCDEFGHI':
    if (int(f'11A{x}3', 19) + int(f'12{x}345', 19))%14==0:
        print(x,(int('11A'+ x + '3', 19) + int('12' + x + '345', 19))//14)
'''

'''from string import*
for x in printable[:20]:
    if (int(f'13{x}cf',20) + int(f'47gh{x}',20)) % 19 == 0:
        print(x,(int(f'13{x}cf',20) + int(f'47gh{x}',20))/19)'''

'''from string import*
for x in printable[:17]:
    if (int(f'18{x}ae',17)+int(f'733{x}c',17)) % 13 == 0:
        print(x, (int(f'18{x}ae',17)+int(f'733{x}c',17)) / 13)'''

'''from string import*
for x in printable[:37]:
    if (int(f'32{x}4',37) + int(f'5{x}29',37)) % 63 == 0:
        print(x, (int(f'32{x}4',37) + int(f'5{x}29',37)) / 63)'''

'''from string import*
for x in printable[:20]:
    for y in printable[:20]:
        if (int(f'A{y}116B{x}F',20) + int(f'4{x}D',20)) % int('10',2) != 0:
            break
    else:
        print(x,(int(f'A2116B{x}F',20) + int(f'4{x}D',20)) // int('10',2))'''

