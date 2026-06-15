#Задачи на двойные указатели
f = open('_24_1.txt')
s = f.readline()
res = []
for l in range(len(s)):
    if s[l] == 'D':
        cnt = 0
        for r in range(l + 1,len(s)):
            if s[r] == 'D':
                break
            if s[r] in '02468':
                cnt += 1
            if cnt > 16:
                break
            if cnt == 16:
                res.append(r-l+1)
print(max(res))

'''f = open('_24_2.txt')
s = f.readline()
res = []
for l in range(len(s)):
    if s[l] == 'R':
        cnt = 0
        for r in range(l + 1,len(s)):
            if s[r] == 'R':
                break
            if s[r] in '13579':
                cnt += 1
            if cnt > 23:
                break
            if cnt == 23:
                res.append(r-l+1)
print(max(res))'''

'''f = open('_24_3.txt')
s = f.readline()[::-1]
res = []
for l in range(len(s)):
    if s[l] != 'H':
        continue
    cnt = 0
    for r in range(l + 1,len(s)):
        if s[r] == 'H':
            break
        if s[r] in '13579':
            cnt += 1
        if cnt > 34:
            break
        if cnt == 34:
            res.append(r-l+1)
print(max(res))'''

'''f = open('_24_4.txt')
s = f.readline()
res = []
for l in range(len(s)):
    if s[l].isdigit():
        continue
    for r in range(l + 1,len(s)):
        if s[r] == s[l]:
            res.append([r-l+1,l])
            break
        if s[r].isalpha():
            break
res.sort(reverse = True)
print(max(res[:5]))'''

