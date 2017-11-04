#!/usr/bin/env python

def reverse(string):
    length = len(string)
    rev = string[length-1]
    for x in range (1,length):
        rev += string[(length-1-x)]
    return rev

string = input("Please enter a string: ")
revString = reverse(string)
print (revString)
        

