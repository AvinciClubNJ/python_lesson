#!/usr/bin/env python
import sys
import math #Cuz why not?
#Find prime numbers between 100 and 200
primelist = []
print("Welcome to the prime number generator!")
while True:
    try:
        input1 = int(input("Enter the starting number: "))
    except ValueError:
        print("Not a number!")
        continue
    if input1 <= 1:
        print("Too less!")
        continue
    break
while True:
    try:
        input2 = int(input("Enter the ending number: "))
    except ValueError:
        print("Not a number!")
        continue
    if input2 < input1:
        print("Less than the starting number!")
        continue
    break
for x in range(input1, (input2+1)):
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
