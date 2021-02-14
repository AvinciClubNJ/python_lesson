with open('paint.in', 'r') as fin:
    l1 = fin.readline().split()
    l2 = fin.readline().split()
    fin.close()
fout = open('paint.out', 'w')
l = [[int(l1[0]), int(l1[1])], [int(l2[0]), int(l2[1])]]
l = sorted(l)
l2 = []
for x in range(len(l)):
    l2.append(l[x][0])
    l2.append(l[x][1])
if l2[1] < l2[2]:
    print((l2[1]-l2[0])+(l2[3]-l2[2]), file=fout)
else:
    print(max(l2)-min(l2), file=fout)
fout.close()
