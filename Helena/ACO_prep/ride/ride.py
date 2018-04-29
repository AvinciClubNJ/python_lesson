'''
ID: helenaz1
LANG: PYTHON3
TASK: ride
'''
with open('ride.in') as f:
    y = []
    for i in range(0,2):
        product = 1
        line = f.readline().strip('\n')
        for x in range(0,len(line)):
            product *= (ord(line[x])-64)
        y.append(product%47)
    f.close

with open ('ride.out','a') as f:
    if y [0] == y[1]:
        f.write("GO")
    else:
        f.write('STAY')
    f.write('\n')
    f.close()
    
            
