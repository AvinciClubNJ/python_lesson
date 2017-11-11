#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

userinput = raw_input("What letter?\n")
goodinput = False
if len(userinput) > 1:
	print("Please imput one letter.")
elif isinstance(userinput, str) == False:
	print("Please imput a letter.")
elif (userinput >= 'a' and userinput <= 'z') != True:
	print("Please imput a lowercase letter.")
else: 
	goodinput = True

if goodinput != True:
	print("Try again.")
elif goodinput == True:
	width = input("Enter an odd base width < 20.\n")
elif isinstance(width, int) == False:
	print("Please imput an integer.")
elif width < 1:
	print("Please imput a positive integer.")
elif width > 20:
	print("Please imput a integer smaller than 20.")
elif width%2 == 0:
	print("Please imput an odd integer.")

if goodinput == True:	
	for x in range(1,width):
		print(" "*((width+1)-x-2)+userinput*(x*2-1))