'''
ID: helenaz1
LANG: PYTHON3
TASK: namenum
'''
ix = {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9}
with open('dict.txt') as f:
    names = []
    for i in range(0,4617):
        names.append(f.readline().strip('\n'))
    names.sort(key=len)
    f.close()
with open('namenum.in') as f:
    num = int(f.readline().strip('\n'))
    f.close()

search = []
for i in range(0,4617,int(4617/27)):
    section = names[0+i:171+i]
    if len(section[170]) >= len(str(num)) and len(section[0]) <= len(str(num)):
        search.extend(section)
names = []
for i in search:
    if len(i) == len(str(num)) and 'Q' not in i and 'Z' not in i:
        status = 0
        for j in range(len(str(num))):
            if ix[i[j]] == int((str(num))[j]):
                status += 1
            else:
                break
        if status == len(str(num)):
            names.append(i)
if len(names) == 0:
    names.append('NONE')
            
with open('namenum.out','a') as f:
    for i in names:
        f.write(i)
        f.write('\n')
    f.close()
    
