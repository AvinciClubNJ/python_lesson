#!/usr/bin/env python

def primeNumber(low,high):
    prime = []
    high1 = int(high**(1/2))
    num = list(range(low,high+1))
    for y in num:
        r = False
        if y<high1:
            for x in range(2,low+1):
                if y%x == 0:
                    r = True
                    break
                else:
                    r = False
        if y >= high1:
             for x in range(2,high1+1):
                if y%x == 0:
                    r = True
                    break
                else:
                    r = False
        if r == False:
            prime.append(y)
    return prime

for i in range(1,4):
    lower = int(input("Enter lower value: "))
    upper = int(input("Enter upper value: "))
    primeList = primeNumber(lower, upper)
    print(primeList)
 

