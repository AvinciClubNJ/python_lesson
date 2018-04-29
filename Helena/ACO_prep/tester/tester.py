with open('tester.in') as f:
    lineOne = f.readline().strip('\n')
    lineTwo = f.readline().strip('\n')
    f.close()
with open('tester.out','a') as f:
    f.write(lineOne)
    f.write('\n')
    f.write(lineTwo)
    f.close()
