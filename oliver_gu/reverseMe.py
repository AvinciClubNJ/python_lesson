#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

userinput = input("Please imput a string.\n")

y = ""

for x in range(0, len(userinput)):
    y = y + userinput[len(userinput)-1-x]

print(y)