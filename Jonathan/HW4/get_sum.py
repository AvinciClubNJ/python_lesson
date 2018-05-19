#!/usr/bin/env python3

mysum = 0

def get_sum(start,end):

	sum = 0
	for i in range(start, end+1):
		sum = sum+i
	return sum
index = 0
while index < 3:
	startNum= int(input("Enter start: "))
	endNum= int(input("Enter end: "))
	mysum = get_sum(startNum,endNum)
	print ("sum of numbers from ", startNum, " to ", endNum, "is: ", mysum)
	index += 1
