num1 = int(input ('Enter the first value: '))
num2 = int(input ('Enter the second value: '))
def getPrimeNumber(num1, num2): 
    for num in range(num1, num2+1):
        if num > num1 + 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print (num)

getPrimeNumber(num1, num2)
