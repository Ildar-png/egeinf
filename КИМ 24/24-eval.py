f = open()
res = []
for i, s in enumerate(f, start = 1): #enumerate нумерует каждую i, start = с чего начинается счет. В итоге получается 2 значения: элемент списка f - i и его порядковый номер s
    try: #Пробует запустить
        if eval(s): #eval возвращает 1 если s при запуске не выдает ошибок, иначе 0
            res.append([len(s),i])
    except: #После вот этого прописываются условия, которые выполняются, если try не смог запустится
        pass
print(max(res))


'''f = open()
res = []
for i, s in enumerate(f,start = 1):
    try:
        res.append([eval(s),i])
    except:
        pass
print(max(res))
'''

'''f = open()
s = f.readline()
arifm = ''
maxeval = 0
for i in range(len(s)):
    if s[i] in '789':
        arifm += s[i]
    elif s[i] in '*0' and len(arifm) > 0 and arifm[-1] not in '*-':
        arifm += s[i]
    else:
        arifm = ''
    if len(arifm) > 0 and arifm[-1] in '0789':
        maxeval = max(eval(arifm),maxeval)
'''

'''f = open('24_hometask1.txt')
res = []
for i, s in enumerate(f,start = 1):
    try:
        res.append([eval(s),i])
    except:
        pass
print(max(res))'''

'''f = open('24_hometask2.txt')
res = []
for i, s in enumerate(f,start = 1):
    try:
        res.append([eval(s),i])
    except:
        pass
print(max(res))
'''

'''def clean_minus(s):
    if s[0] == '-':
        stop = min([i for i in range (len(s)) if s[i] in '*+'] + [len(s)]) + 1
        return s[stop:]
    start = s.index('-')
    stop = min([i for i in range (len(s)) if s[i] in '*+' and i > start] + [len(s)])
    return s[:start] + s[stop:]

f = open("24_hometask3.txt")
ans = []
available = '0123456789*+-'
for s in f:
    try:
        s = s.strip()
        if all(x in available for x in s):
            input_s = s
            while '-' in s:
                s = clean_minus(s)
            ans.append([eval(s), input_s])
    except:
        continue
print(max(ans))'''













