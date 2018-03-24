with open('promote.in', 'r') as fin:
    bronze = list(map(int, fin.readline().split()))
    silver = list(map(int, fin.readline().split()))
    gold = list(map(int, fin.readline().split()))
    platinum = list(map(int, fin.readline().split()))
fout = open('promote.out', 'w')

b_s = 0 #Bronze to silver
s_g = 0 #Silver to gold
g_p = 0 #Gold to platinum

for rank in range(4, 0, -1):
    if rank == 4:
        if platinum[1]-platinum[0] > 0: #Is end greater than beginning?
            g_p += platinum[1]-platinum[0] #People that came to plat
    if rank == 3:
        if g_p > 0:
            s_g += gold[1]-(gold[0]-g_p)#The logic here: If people promoted, then you can take the original amount of people in gold and subtract it by the people that promoted.  Then use the amount of people that ended up in gold and subtract that by the number of people that didn't promote.  That will give you the amount of people that had to promote into gold.
    if rank == 2:
        if s_g > 0:
            b_s = silver[1]-(silver[0]-s_g)#Same thing
#Printing the answer
print(b_s, file=fout)
print(s_g, file=fout)
print(g_p, file=fout)

fout.close()
