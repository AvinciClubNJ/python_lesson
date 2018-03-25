#!/usr/bin/env python3

def get_sum(start, end):
    sum = 0
    for i in range (start, end+1):
        sum+=i
    return sum
index = 0
while index < 3:
    startNum = int(input("Enter start: "))
    endNum = int(input("Enter end: "))
    mysum = get_sum(startNum, endNum)
    print("The sum of all the numbers between", startNum, "and", endNum, "is",  mysum, ".")
    index += 1
