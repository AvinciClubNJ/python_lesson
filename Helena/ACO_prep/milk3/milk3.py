'''
ID: helenaz1
LANG: PYTHON3
TASK: milk3
'''
seen, prev = [],[]
def pour(bucket):
    last = [x for x in milk[1]]
    if milk[0][bucket[1]] - milk[1][bucket[1]] >= milk[1][bucket[0]]:
        milk[1][bucket[1]] += milk[1][bucket[0]]
        milk[1][bucket[0]] = 0
    else:
        milk[1][bucket[0]] -= milk[0][bucket[1]]-milk[1][bucket[1]]
        milk[1][bucket[1]] = milk[0][bucket[1]]   
    main(bucket,last)
    return last
def main(previous,lastOne):
    if milk[1] in seen:
        milk[1] = [x for x in lastOne]
        return milk[1]
    toAdd = [x for x in milk[1]]
    seen.append(toAdd)
    for i in step:
        if (i[::-1] == previous or milk[1][i[0]] == 0 or milk[1][i[1]] == milk[0][i[1]]):
            continue
        else:
            milk[1] = pour(i)
with open ('milk3.in') as f:
    A, B, C = [int(x) for x in f.readline().strip('\n').split(' ')]
milk = [[A,B,C],[0,0,C]]
step = [[0,1],[0,2],[1,0],[1,2],[2,0],[2,1]]
main([0,0],prev)
results = []
for i in seen:
    if i[0] == 0 and i[2] not in seen:
        results.append(i[2])
results.sort()
with open('milk3.out','w') as f:
    toPrint = '{}'.format(results[0])
    for i in range(1,len(results)):
        toPrint += " {}".format(results[i])
    f.write('{}\n'.format(toPrint))




            




        
    
        
        
