#!/usr/bin/env python
while True:
    char = input("Please enter a character to build the triangle: ")
    if len(char) > 1:
        print("One character please")
        continue
    elif char >= 'a' and char <= 'z':
        char2 = char
        break
    else:
        print("A number from a to z please")
while True:
    try:
        width = int(input("Please enter in the triangle width(odd number only): "))
    except ValueError:
        print("Not a number please enter again!")
        continue
    if width > 20:
        print("That is too big!")
        continue
    if width % 2 == 0:
        print("It is even, enter again")
        continue
    else:
        break

height = (width + 1)/2

#Create da triangle
for x in range(0, int(height)):
    space = " " * int(((width-1)/2) - x)
    character = char2 * int((x*2) + 1)
    print(space, character)
print("\n")
#Create da UPSIDE down ∆
for x in range(int(height), 0, -1):
    space = " " * int(((width+1)/2) -x )
    character = char * int((x*2)-1)
    print(space, character)
