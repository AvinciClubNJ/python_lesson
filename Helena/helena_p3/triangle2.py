#!/usr/bin/env python

while True:
    userIn = input("Please enter a char to build the triangle: ")
    if len(userIn) > 0:
        c = userIn[0]
        c = ord(c)
    if (c >= ord('a') and c <= ord('z')):
        break
    else:
        continue

while True:
    widthIn = input("Please enter the triangle base width, odd numer only: ")
    if len(widthIn) == 0:
        continue

    width = int(widthIn)
    if (width % 2 == 0):
        continue
    else:
        if(width>=20):
            continue
        else:
            break

height = (width + 1) / 2
c = chr(c)

for x in range (0, int(height)):
    spaceToPrint = " "*int(((width-1)/2)-x)
    charToPrint = c * int((x*2)+1)
    print(spaceToPrint, charToPrint)

print()

for x in range (int(height), 0, -1):
    spaceToPrint = " " *int(((width+1)/2)-x)
    charToPrint = c*int((x*2)-1)
    print(spaceToPrint, charToPrint)
