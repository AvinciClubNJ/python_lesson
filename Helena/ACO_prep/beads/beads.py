'''
ID: helenaz1
LANG: PYTHON3
TASK: beads
'''
with open('beads.in') as f:
    number = int(f.readline().strip('\n'))
    lace = f.readline().strip('\n')
    f.close()
change = 0
current = ''
chain = ''
section = []
for i in lace:
    if (i == 'b' or i == 'r') and current != i:
        current = i
        change += 1
if change >= 3:
    lace = lace+lace
    section = []
    change = 0
    current = ''
    chain = ''
    for i in lace:
        if (i == 'b' or i == 'r') and current != i:
            current = i
            change += 1
        if change <= 1:
            chain = chain + i
        else:
            section.append(chain)
            chain = i
            current = ''
            if i == 'b' or i == 'r':
                change = 1
                current = i
            else:
                change = 0
lengths = []
for i in range(0,len(section)-1):
    if section[i][len(section[i])-1] == 'w' and (len(section[i])<len(section[i+1]) or len(section[i])>len(section[i+1])):
        section[i] = section[i][:-1]
        section[i+1] = 'w' + section[i+1]
        if len(section[i])+1 == len(section[i+1]):
            lengths.append(len(section[i])+len(section[i+1])+1)
        else:
            lengths.append(len(section[i])+len(section[i+1]))
    else:
        lengths.append(len(section[i])+len(section[i+1]))

with open('beads.out','a') as f:
    if len(lengths) == 0:
        f.write('%d'%number)
    else:
        f.write("%d"%max(lengths))
    f.write('\n')
    f.close()

