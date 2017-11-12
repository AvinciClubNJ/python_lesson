#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

def get_sum(start, end):
	sum = 0
	for i in range(start, end+1):
		sum = sum + i
	return sum

x = input("Set minimum value. ")
y = input("Set maximum value. " )

while True:
	try:
		a = float(x)
		b = float(y)
	except ValueError:
		print("Invalid imput.")
		continue
	mysum = get_sum(int(x),int(y))
	print("Sum of numbers from " + str(int(x)) +  " to " + str(int(y)) + " inclusive: " + str(mysum))
	break
