'''
ID: helenaz1
LANG: PYTHON3
TASK: skidesign
'''
def calculate(thisRange):
    total = 0
    for i in hills:
        if i < thisRange[0]:
            total+= (thisRange[0]-i)**2
        elif i > thisRange[1]:
            total += (i-thisRange[1])**2
    return total
with open('skidesign.in') as f:
    num = int(f.readline().strip('\n'))
    hills = [int(x) for x in f.readlines()]
hills.sort()
checks = [[x,x+17] for x in range(1,101-17)]
with open('skidesign.out','w') as f:
    f.write('{}\n'.format(min([calculate(x) for x in checks])))
    
