'''
ID: helenaz1
LANG: PYTHON3
TASK: milk2
'''
with open('milk2.in') as f:
    num = int(f.readline())
    begin = []
    end = []
    for i in range(0,num):
        time = f.readline().strip('\n').split(' ')
        time = list(map(int,time))
        begin.append(time[0])
        end.append(time[1])
begin.sort()
end.sort()

start = 0
i = 0
j = 0
idle = []
cont = []
while begin[i] <= max(begin):
    if i == num-1:
        cont.append(end[i]-begin[i])
        break
    i += 1
    checkBegin = begin[i]
    checkEnd = end[j]
    while checkBegin <= checkEnd:
        if i < num -1 and j < num -1:
            i += 1
            j+= 1
            checkBegin = begin[i]
            checkEnd = end[j]
        elif j<num -1:
            j += 1
            checkEnd = end[j]
        else:
            break
    if checkBegin-checkEnd < 0:
        idle.append(0)
    else:
        idle.append(checkBegin-checkEnd)
    checkBegin = begin[start]
    cont.append(checkEnd-checkBegin)
    if checkEnd == end[j]:
        j += 1
    start = j
with open('milk2.out','a') as f:
    f.write('%d'%max(cont))
    f.write(' ')
    if len(idle) == 0:
        f.write('%d'%0)
    else:
        f.write('%d'%max(idle))
    f.write('\n')

    


