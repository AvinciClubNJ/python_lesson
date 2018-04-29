'''
ID: helenaz1
LANG: PYTHON3
TASK: milk
'''
with open('milk.in') as f:
    info = f.readline().strip('\n').split(' ')
    info = list(map(int,info))
    amount = info[0]
    num = info[1]
    farmers = []
    for i in range(num):
        farm = list(map(int,f.readline().strip('\n').split(' ')))
        farmers.append(farm)
    f.close()
farmers = sorted(farmers,key = lambda x:x[0])
price = 0
for i in farmers:
    if amount < i[1]:
        price += amount*i[0]
        amount -= amount
        break
    else:
        price += i[1]*i[0]
        amount -= i[1]
with open('milk.out','a') as f:
    f.write('%d'%price)
    f.write('\n')
    f.close()

