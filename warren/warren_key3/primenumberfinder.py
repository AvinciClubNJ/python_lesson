#!/usr/bin/env python
import sys
import math #Cuz why not?
#Find prime numbers between 100 and 200
primelist = []
for x in range(12, 401):
    addthing = False
    for y in range(2, x):
        if x % y == 0:
            addthing = False
            break
        else:
            addthing = True
    if addthing == True:
        primelist.append(x)
print(primelist)
print("Length of list: %s" % len(primelist))
