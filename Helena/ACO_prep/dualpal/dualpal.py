'''
ID: helenaz1
LANG: PYTHON3
TASK: dualpal
'''
def modDivision(dividend,base):
    result = ''
    while dividend > 0:
        next = dividend%base
        result += (str(next))
        dividend = int(dividend/base)
    return result

def checkPal(number):
    for i in range(int(len(number)/2)):
        if number[i] != number[len(number)-1-i]:
            return False
    return True

with open('dualpal.in') as f:
    info = f.readline().strip('\n').split(' ')
    info = list(map(int,info))
    num = info[0]
    start = info[1]
    f.close()
with open('dualpal.out','a') as f: 
    add = 0
    while add < num:
        start += 1
        check = 0
        for j in range(2,11):
            if checkPal(modDivision(start,j)) == True:
                check+=1
            if check == 2:
                add += 1
                f.write('%d'%start)
                f.write('\n')
                break
        
