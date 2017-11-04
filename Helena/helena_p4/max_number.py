#!/usr/bin/env python

numbers = [1,-20,0,100,-5,4,10,23,-19,99]
length = len(numbers)
print(max(numbers))

num = []
'''
for x in numbers:
    for y in numbers:
        if y > x:
            num.append(y)
        elif y < x:
            num.remove(y)
print(num)
'''

for y in numbers[0:]:
    
    '''
    for x in numbers[1:]:
        if x >= y:
            num.append(x)
        elif x < y:
            num.remove(x)
print (num)
'''

