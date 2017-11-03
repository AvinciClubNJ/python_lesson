import math

Number = int(input("Type in a number: "))
CheckLimit = int(math.sqrt(Number))
PossiblePrimeNumbers = list(range(Number + 1))
PossiblePrimeNumbers[0:2] = [0, 0]
for i in PossiblePrimeNumbers:
    if i > 1 and i <= CheckLimit:
        y = 2
        ReachedLimit = i * y
        while ReachedLimit < len(PossiblePrimeNumbers):
            PossiblePrimeNumbers[i*y] = 0 
            y += 1
            ReachedLimit = i * y
    
y = 0

while y != len(PossiblePrimeNumbers):
    if PossiblePrimeNumbers[y] == 0:        
        del PossiblePrimeNumbers[y]
    else:  
        y += 1
    
    

print ("Your prime Numbers are:", PossiblePrimeNumbers)
        

