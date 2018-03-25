lines = []
with open("speeding.in") as fin:
	lines = fin.readlines()
N, M = (int(x) for x in lines[0].split())	
limitdistance = []
limitspeed = []
bessiedistance = []
bessiespeed = []

for i in range(N):
	d, s = (int(x) for x in lines[i+1].split())
	limitdistance.append(d)
	limitspeed.append(s)

for i in range(M):
	d, s = (int(x) for x in lines[i+N+1].split())
	bessiedistance.append(d)
	bessiespeed.append(s)
bessie = []
limit = []
over = []
for i in range(M):
	for j in range(bessiedistance[i]):
		bessie.append(bessiespeed[i])
for i in range(N):
	for j in range(limitdistance[i]):
		limit.append(limitspeed[i])

for i in range(100):
	if bessie[i] > limit[i]:
		over.append(bessie[i] - limit[i])
	else:
		over.append(0)
x = max(over)

fout = open ('speeding.out', 'w')

fout.write (str(x) + '\n')

fout.close()
