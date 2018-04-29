'''
ID: helenaz1
LANG: PYTHON3
TASK: barn1
'''
with open('barn1.in') as f:
    info = list(map(int,f.readline().strip('\n').split(' ')))
    panels = info[0]
    size = info[1]
    num = info[2]
    cows = []
    for i in range(num):
        cows.append(int(f.readline().strip('\n')))
    cows.sort()
    f.close()
space = []
for i in range(num-1):
    space.append(cows[i+1]-cows[i])
skips = []
temp = list(space)
for i in range(panels-1):
    if num <= panels:
        break
    toDel = max(temp)
    skips.append(toDel)
    temp.remove(toDel)
init = 0
total = 0
if num <= panels:
    total = num
for i in space:
    if num <= panels:
        break
    if i in skips:
        total += cows[space.index(i)] - cows[init] +1
        init = space.index(i)+1
        skips.remove(i)
if num > panels:
    total += cows[num-1] - cows[init] +1
with open('barn1.out','a') as f:
    f.write('%d'%total)
    f.write('\n')
    f.close()

