'''
ID: helenaz1
LANG: PYTHON3
TASK: friday
'''
with open ('friday.in') as f:
    years = int(f.readline().strip('\n'))
    f.close()

days = {1:0,2:0,3:0,4:0,5:0,6:0,0:0}
months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
start = 0
for i in range(0,years):
    if ((i+1900) % 4 == 0 and (i+1900)%100 != 0) or (i+1900)%400 == 0:
        months[2] = 29
    else:
        months[2]= 28
    for y in range(1,13):
        toAdd = (13+(start)) % 7
        days[toAdd] += 1
        start = (start+months[y]) % 7 

with open('friday.out','w') as f:
    for i in range(6,12):
        f.write('%d'%days[(i%7)])
        f.write(' ')
    f.write('%d'%days[5])
    f.write('\n')
