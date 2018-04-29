'''
ID: helenaz1
LANG: PYTHON3
TASK: transform
'''
with open ('transform.in') as f:
    num = int(f.readline().strip('\n'))
    original = []
    new = []
    for i in range(num):
        original.append(f.readline().strip('\n'))
    for i in range(num):
        new.append(f.readline().strip('\n'))
    f.close()

def checkOne(compare):
    for i in range(num):
        for j in range (num):
            if ord(compare[i][j]) != ord(new[j][num-1-i]):
                return False
    return True

def checkTwo(compare):
    for i in range(num):
        for j in range(num):
            if ord(compare[i][j]) != ord(new[num-1-i][num-1-j]):
                return False
    return True

def checkThree(compare):
    for i in range(num):
        for j in range(num):
            if ord(compare[i][j]) != ord(new[num-1-j][i]):
                return False
    return True


def checkFour():
    for i in range(num):
        for j in range(num):
            if ord(new[i][j]) != ord(original[i][num-1-j]):
                return False
    return True
def checkFive():
    flipped = []
    for i in range(num):
        string = ''
        for j in range(num):
            string = string+ (original[i][num-1-j])
        flipped.append(string)
    if checkOne(flipped) == True or checkTwo(flipped) == True or checkThree(flipped) == True:
        return True
    else:
        return False
    

def checkSix():
    for i in range(num):
        for j in range(num):
            if ord(original[i][j]) != ord(new[i][j]):
                return False
    return True

answer = 7
if checkOne(original) == True:
    answer = 1
else:
    if checkTwo(original) == True:
        answer = 2
    else:
        if checkThree(original) == True:
            answer = 3
        else:
            if checkFour() == True:
                answer = 4
            else:
                if checkFive() == True:
                    answer = 5
                else: 
                    if checkSix() == True:
                        answer = 6
                    else: 
                        answer = 7
with open('transform.out','a') as f:
    f.write('%d'%answer)
    f.write('\n')
    f.close()

