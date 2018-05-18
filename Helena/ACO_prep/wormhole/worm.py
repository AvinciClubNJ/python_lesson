'''
ID: helenaz1
LANG: PYTHON3
TASK: wormhole
'''
total = 0
def partner():
    i = 1
    total = 0
    for i in range(1,14):
        if i not in pairings:
            break
    if i > num:
        result = check()
        if result:
            return 1
        return 0
    for j in range(i+1,num+1):
        if pairings[j] == 0:
            pairings[i] = j
            pairings[j] = i
            total+=partner()
            pairings[i],pairings[j] = 0,0
    return total
def check():
    for x in range(1,num+1):
        pos = x
        for _ in range(num):
            pos = connection[pairings[pos]]
        if pos != 0:
            return True
    return False
with open('wormhole.in') as f:
    num = int(f.readline().strip('\n'))
    holes = [[x for x in range(num+1)],[0],[0]]
    for i in range(num):
        x,y = [int(j) for j in f.readline().strip('\n').split(' ')]
        holes[1].append(x)
        holes[2].append(y)
connection = [0 for _ in range(num+1)]
for i in range(1,num+1):
    for j in range(1,num+1):
        if holes[2][i] == holes[2][j] and holes[1][j] > holes[1][i]:
            if connection[i] == 0 or holes[1][j]-holes[1][i] < holes[1][connection[i]]-holes[1][i]:
                connection[i] = j
pairings = [0 for _ in range(num+1)]
with open('wormhole.out','w') as f:
    f.write('{}\n'.format(partner()))
