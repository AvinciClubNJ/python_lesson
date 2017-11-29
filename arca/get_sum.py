#!/usr/bin/env python

def get_sum(start, end):
    sum = 0 
    for i in range(start, end+1):
        sum = sum +i
    return sum
    print("sum1: ", sum1)
    print("mysum: ", mysum)
    return sum1

index = 0
while index < 1:
    startNum = int(input("'Enter start: "))
    endNum = int(input("Enter end: "))
    mysum = get_sum(startNum, endNum)
    print ("sum of numbers between ", startNum, " to ", endNum, "; ",mysum, ".")
    index += 1     
