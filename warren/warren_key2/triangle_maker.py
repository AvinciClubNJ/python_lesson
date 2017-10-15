import sys
while True:
    letter = input("Enter in a something to make the triangle out of: ")
    if len(letter) > 1:
        print('Only one letter/symbol/number please!')
        continue
    break
while True:
    try:
        number = int(input("Enter in an odd number for the width of the triangle: "))
    except:
        print("Enter an odd number!")
        continue
    if number % 2 == 0:
        print("Enter in a odd number please!")
        continue
    break
y = 1
height = number + 1
height = height / 2
for x in range(0, int(height)):
    print(' ' * number, letter * y)
    number -= 1
    y = y + 2
print('')
y -= 2
number += 1
for x in range(0, int(height)):
    print(' ' * number, letter * y)
    number += 1
    y = y - 2
