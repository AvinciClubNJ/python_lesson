#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

prisoners = int(input("number of prisoners\n"))

sum = 0

for x in range(1, prisoners + 1):
    sum += nCr(prisoners, x)

print(sum)