#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

for x in range(100,200):
	for y in range(2,x//2):
		if x%y == 0:
			break
	else:
		print(str(x) + " is a prime number.")