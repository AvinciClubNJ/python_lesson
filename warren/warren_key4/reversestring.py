#!/usr/bin/env python
import sys

def reverseMe(line):
    string = ""
    for x in line:
        string = x + string
    return string

inputLine = input("String input: ")

thing = reverseMe(inputLine) #calls the function reverseme
print(thing)

print("Python easy way: ", inputLine[::-1])
