for num in range(100, 201):
    if num > 101:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print (num)


