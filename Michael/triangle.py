#!/usr/bin/env python

while True:
    userIn = input("Please enter a char to build the triangle: ")
    print("userIn=", userIn)
    if len(userIn) > 0:
        for x in range(int("a"), int("z")+1):
            if userIn == x:
                c = userIn[0]
                break
            else:
                print()


while True:
    widthIn = input("Please enter the triangle base width, odd number only: ")
    if len(widthIn) == 0:
        continue

    width = int(widthIn)
    if (width % 2 == 0):
        continue
    else:
        break

height = (width + 1) / 2

# Create triangle
for x in range (0, int(height)):
    spaceToPrint = " " * int(((width-1)/2) - x)
    charToPrint = c * int((x*2)+1)
    print(spaceToPrint, charToPrint)

print()

# Create up side down triangle
for x in range (int(height), 0, -1):
    spaceToPrint = " " * int(((width+1)/2) - x)
    charToPrint = c * int((x*2)-1)
    print(spaceToPrint, charToPrint)