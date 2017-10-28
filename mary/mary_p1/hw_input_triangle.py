i = 0
x = 1
letter = input("Enter a char from a to z inclusive")
mystr = "abcdefghijklmnopqrstuvwxyz"
if letter[0] in mystr:
    while i!= 5:
        triangle = (5-x) * " " + letter + "  " * i + letter
        print( triangle)
        i+=1
        x+=1
triangle = letter *(i*2)
print(triangle)
