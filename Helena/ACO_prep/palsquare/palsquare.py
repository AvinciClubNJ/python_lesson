'''
ID: helenaz1
LANG: PYTHON3
TASK: palsquare
'''
digits = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J'}
with open('palsquare.in') as f:
    base = int(f.readline().strip('\n'))
    f.close()

def modDivision(dividend):
    result = ''
    while dividend > 0:
        next = dividend%base
        if next >=10:
            result += (digits[next])
        else:
            result += (str(next))
        dividend = int(dividend/base)
    result = result[::-1]
    return result

def checkPal(number):
    for i in range(int(len(number)/2)):
        if number[i] != number[len(number)-1-i]:
            return False
    return True

with open('palsquare.out','a') as f:
    for num in range(1,301):
        check = num **2
        squared = modDivision(check)
        final = checkPal(squared)
        if final == True:
            f.write(modDivision(num))
            f.write(' ')
            f.write(squared)
            f.write('\n')
    f.close()