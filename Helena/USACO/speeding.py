with open('speeding.in') as f:
    info = list(map(int,f.readline().strip('\n').split(' ')))
    speed = []
    actual = []
    for i in range(info[0]):
        speed.append(list(map(int,(f.readline().strip('\n').split(' ')))))
    for i in range(info[1]):
        actual.append(list(map(int,(f.readline().strip('\n').split(' ')))))
    f.close()
violations = []
distance = [speed[0][0],actual[0][0]]
spood = [speed[0][1],actual[0][1]]
position = [0,0]
for i in range(100):
    if i >= distance[0]:
        position[0]+=1
        distance[0]+=speed[position[0]][0]
        spood[0]=speed[position[0]][1]
    if i >= distance[1]:
        position[1]+=1
        distance[1]+=actual[position[1]][0]
        spood[1]=actual[position[1]][1]
    if spood[1]>spood[0]:
        if (spood[1]-spood[0]) not in violations:
            violations.append(spood[1]-spood[0])
toPrint = 0
if len(violations) != 0:
    toPrint = max(violations)
with open('speeding.out','a') as f:
    f.write('%d'%toPrint)
    f.write('\n')
    f.close()