#!/usr/bin/env python
prime = []
while True:
    lower = int(input("Please enter lower value: "))
    if lower >= 0:
        break
    else:
        print("Please enter a number.")
        continue
while True:
    upper = int(input("Please enter upper value: "))
    if upper > lower:
        break
    else:
        print("Upper value must be greater than lower value.")
        continue

upper1 = int(upper**(1/2))
num = list(range(lower,upper+1))
for y in num:
    r = False
    if y < upper1:
        for x in range(2,lower+1):
            if y%x == 0:
                r = True 
                break
            else:
                r = False
    if y >= upper1:
        for x in range(2,upper1+1):
            if y%x == 0:
                r = True
                break
            else:
                r = False
    if r == False:
        prime.append(y)
print(prime)
print("there are ", len(prime) ," prime numbers.")
