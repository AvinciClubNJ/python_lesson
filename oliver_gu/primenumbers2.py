#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

goodinput = False

while goodinput == False:
    try:
        minimum = input("Enter minimum value.\n") 
        if isinstance(int(minimum), int):
            goodinput = True
            break
        else:
            goodinput = False
            print("Please input an integer.")
    except ValueError:
        print("Please input a number.")
        continue

while True:
    try: 
        maximum = input("Enter maximum value.\n")
        if isinstance(int(maximum), int):
            if maximum <= minimum:
                goodinput = False
                print("Please imput a value greater than the minimum.")
            else:
                goodinput = True
                break
        else:
            goodinput = False
            print("Please imput an integer.")
    except ValueError:
        print("Please input a number.")
        continue

for x in range(int(minimum), int(maximum) + 1):
	for y in range(2,x//2+1):
		if x%y == 0:
			break
	else:
		print(str(x) + " is a prime number.")