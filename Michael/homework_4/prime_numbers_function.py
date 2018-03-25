#!/usr/bin/python3
def GetPrimeNumber (a, b):
    list1=[]
    for x in range(a, b+1):
        for y in range(2, x+1):
            if (x%y) == 0:
                break
        if y==x:
            list1.append(x)
    return list1

for x in range (0, 3):
   start_num = int(input("Please enter the starting number of this list (it must be at least two): "))
   end_num = int(input("Enter the ending number of this list: "))
   the_prime_numbers = GetPrimeNumber(start_num, end_num)
   print("The prime numbers between ", start_num, " and ", end_num, " are ", the_prime_numbers)