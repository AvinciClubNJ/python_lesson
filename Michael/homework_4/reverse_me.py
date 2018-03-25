#!/usr/bin/python3

def reverseMe(s):
    x = len(s)
    str1 = ''
    while x > 0:
        x -= 1 
        str1 = str1 + s[x]
    return str1

str2 = reverseMe('Hello')
print('reverse of Hello is: ', str2)