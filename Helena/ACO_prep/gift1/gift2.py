'''
ID: helenaz1
LANG: PYTHON3
TASK: gift1
'''
with open('gift1.in','r') as f:
    num = int(f.readline().strip('\n'))
    name = {}
    ordered = []
    for i in range(0,num):
        name[f.readline().strip('\n')] = 0
        print(name)
    for j in range(0,len(name)):
        giver = f.readline().strip('\n')
        amount = f.readline().strip('\n').split(' ')
        amount = list(map(int,amount))
        receiver = []
        for x in range(0,amount[1]):
            receiver.append(f.readline().strip('\n'))
        name[giver] -= amount[0]
        if amount[0] == 0:
            pass
        else:
            for y in receiver:
                name[y] += int(amount[0]/amount[1])
            name[giver] += amount[0]% amount[1]
    f.close()
with open('gift1.out','a') as g:
    for k in name:
        g.write(k)
        g.write(' ')
        g.write('%d'%name[k])
        g.write('\n')
    g.close()
        