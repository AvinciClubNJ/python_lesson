#!/usr/bin/env python
import sys
import math #Cuz why not?
print("Welcome to the prime number generator!")

def primenumberfind(input1, input2):
    primelist = []
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
    return primelist

for x in range(1, 4):
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
    prime = primenumberfind(input1, input2)
    
    print(prime)
    print("Length of list: %s" % len(prime))
print("Goodbye.")
