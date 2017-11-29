num1 = int(input ('Enter the first value: '))
num2 = int(input ('Enter the second value: '))
def getPrimeNumber(num1, num2): 
    for num in range(num1, num2):
        if num > num1:
            for i in range(2, num2):
                if (num % i) == 0:
                    break
        else:
            print (num)
getPrimeNumber(num1, num2)

