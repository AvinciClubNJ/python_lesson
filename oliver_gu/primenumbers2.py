#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

goodinput = False

while goodinput == False:
    try:
         minimum = input("Enter minimum value.\n")
    except NameError:
        print("Please input a number.")
        continue
    if isinstance(minimum, int):
        goodinput = True
        break
    else:
        goodinput = False
        print("Please input an integer.")

while True:
    try: 
        maximum = input("Enter maximum value.\n")
    except NameError:
        print("Please input a number.")
        continue
    if isinstance(maximum, int):
        if maximum <= minimum:
            goodinput = False
            print("Please imput a value greater than the minimum.")
        else:
            goodinput = True
            break
    else:
        goodinput = False
        print("Please imput an integer.")

for x in range(minimum,maximum+1):
	for y in range(2,x//2+1):
		if x%y == 0:
			break
	else:
		print(str(x) + " is a prime number.")