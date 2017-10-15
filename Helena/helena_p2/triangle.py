letter = input("Enter a body.")
space = " "
count = 1
while count == 1:
    width = int(input("Enter an odd number width."))
    if width % 2 == 0:
        print("Error, please try again")
    if width % 2 == 1:
        height = int((width+1)/2)
        count += 1

for h in range(1,height+1):
    print(space*(height-h)+(2*h-1)*letter)
print()
for h in range(1,height+1):
    print(space*(h-1)+letter*(2*height+1-2*h))
print()
print("Goodbye.")

