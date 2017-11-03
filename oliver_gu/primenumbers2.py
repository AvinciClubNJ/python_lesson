#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

goodinput = False

while goodinput == False:
    minimum = input("Enter minimum value.\n")
    if isinstance(minimum, int) or isinstance(minimum, float):
        goodinput = True
        break
    else:
        goodinput = False
        print("Please input a number.")

while goodinput == False:
    maximum = input("Enter maximum value.\n")
    if isinstance(int(maximum), int) or isinstance(float(maximum), float):
        if maximum <= minimum:
            goodinput = False
            print("Please imput a value greater than the minimum.")
        else:
            goodinput = True
            break
    else:
        goodinput = False
        print("Please imput a number.")

for x in range(minimum,maximum+1):
	for y in range(2,x//2):
		if x%y == 0:
			break
	else:
		print(str(x) + " is a prime number.")