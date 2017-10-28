#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
"""
L = raw_input("How many levels?\n")
try:
	L = int(L)
except Exception as e:
	print("Invalid number")
else:
	print("This is an int!")
	# Do Stuff Here
"""
L = raw_input("How many levels?\n")
if L < 2:
  print("Invalid number")
elif type(L)==int:
  for x in range(0,L-1):
	print(" "*(L-x-1)+"/"+" "*(2*x)+"\\")
  print("/"+"_"*2*(L-1)+"\\")
else:
	print("alex is a fat poop")