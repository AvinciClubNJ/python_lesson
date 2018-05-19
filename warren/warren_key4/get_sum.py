#!/usr/bin/env python

def get_sum(start, end):
	sum = 0
	for x in range(start, end+1):
		sum += x 
	return sum
index = 0
while index < 3:
	startNum = int(input("Enter start: "))
	endNum = int(input("Enter end : "))
	mysum = get_sum(startNum, endNum)
	print("sum of numbers between ", startNum, " and ", endNum, ": ", mysum)
	index += 1
