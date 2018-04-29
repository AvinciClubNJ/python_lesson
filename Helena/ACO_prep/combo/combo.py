'''
ID: helenaz1
LANG: PYTHON3
TASK: combo
'''
def check(digit,ok):
    aList = []
    for x in range(-2,3):
        add = digit+x
        while add <= 0:
            add += num
        while add > num:
            add -= num
        if add not in aList:
            aList.append(add)
    ok.append(aList)
    return ok

with open('combo.in') as f:
    num = int(f.readline().strip('\n'))
    comboOne = list(map(int,f.readline().strip('\n').split(' ')))
    comboTwo = list(map(int,f.readline().strip('\n').split(' ')))
    f.close()
jOk= []
cOk= []
for i in comboOne:
    jOk = check(i,jOk)
for i in comboTwo:
    cOk = check(i,cOk)
correct = [jOk,cOk]

solutions = []
for h in correct:   
    for i in h[0]:
        for j in h[1]:
            for k in h[2]:
                add = [i,j,k]
                if add not in solutions:
                    solutions.append(add)
print (solutions)
with open('combo.out','a') as f:
    f.write('%d'%len(solutions))
    f.write('\n')
    f.close()
