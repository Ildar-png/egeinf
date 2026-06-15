'''f = open('26.3_Kt3PdLv.txt')
k = int(f.readline())
n = int(f.readline())
files = []
cnt, lastdisk = 0, 0
for s in f:
    start,end = map(int,s.split())
    files.append([start,end])
files.sort()
disks = [0]*k
for start, end in files:
    for i in range(k):
        if start > disks[i]:
            disks[i] = end
            cnt += 1
            lastdisk = (i+1)
            break
print(cnt,lastdisk)'''

f = open('26.2_4BXGFng.txt')
n = int(f.readline())
startlent = []
endlent = []
for i in range(n):
    shlif,okr = map(int, f.readline().split())
    if shlif < okr:
        startlent.append(([shlif,i+1]))
    else:
        endlent.append(([okr, i + 1]))
startlent.sort()
endlent.sort()
print(max(startlent),max(endlent))
print(len(endlent)-1)