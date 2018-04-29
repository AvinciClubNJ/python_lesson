'''
ID: helenaz1
LANG: PYTHON3
TASK: crypt1
'''

def calculate():
    firstNums = [i,j,k]
    first = ''
    secondNums = [l,m]
    second = ''
    for x in firstNums:
        first += str(x)
    first = int (first)
    for x in secondNums:
        second += str(x)
    second = int(second)
    if calcProduct(first,second) == False:
        return False
    else:
        return True
    
def calcProduct(a,b):
    products = []
    for y in range(2):
        prod = a*int(str(b)[y])
        if len(str(prod)) > 3:
            return False
        for z in str(prod):
            if int(z) not in sequence:
                return False
        products.append(prod)
    final = products[0]*10+products[1]
    if len(str(final)) > 4:
        return False
    for z in str(final):
        if int(z) not in sequence:
            return False
    return True

with open ('crypt1.in') as f:
    num = int(f.readline().strip('\n'))
    sequence = list(map(int,f.readline().strip('\n').split(' ')))
    f.close()

success = 0
for i in sequence:
    for j in sequence:
        for k in sequence:
            for l in sequence:
                for m in sequence:
                    if calculate() == True:
                        success += 1
with open('crypt1.out','a') as f:
    f.write('%d'%success)
    f.write('\n')
    f.close()
