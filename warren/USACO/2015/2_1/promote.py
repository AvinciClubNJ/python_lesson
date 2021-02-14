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
            g_p += platinum[1]-platinum[0]
    if rank == 3:
        if gold[0]-(platinum[1]-platinum[0]) < gold[1]:
            s_g += gold[1]-(gold[0]-(platinum[1]-platinum[0]))
    if rank == 2:
        if s_g > 0:
            if silver[0]-s_g < silver[1]:
                b_s = silver[1]-(silver[0]-s_g)

print(b_s, file=fout)
print(s_g, file=fout)
print(g_p, file=fout)

fout.close()
