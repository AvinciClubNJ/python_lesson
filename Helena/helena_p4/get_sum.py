#!/usr/bin/env python

def get_sum(start,end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

while True:
    startNum = int(input("Enter a number:"))
    endNum = int(input("Enter a number:"))
    mysum = get_sum(startNum,endNum)
    print ("sum of numbers:", mysum)
