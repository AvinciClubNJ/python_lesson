#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

def get_sum(start, end):
	sum = 0
	for i in range(start, end+1):
		sum = sum + i
	return sum

x = input("Set minimum value. ")
y = input("Set maximum value. " )

goodimput = False
if isinstance(x, number) == True and isinstance(y, number) == True:
	goodimput = True
else:
	print("Invalid imput.")

mysum = get_sum(x,y)
print "Sum of numbers between " + str(x) +  " to " + str(y) + ": " + str(mysum)
