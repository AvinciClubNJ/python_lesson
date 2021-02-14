lines = []

with open("badmilk.in") as fInput:
    lines = fInput.readlines()

N, M, D, S = (int(x) for x in lines[0].split())

SickPeople = []
People = []
Possible = []

for _ in range(S):
    SickPeople.append([])
    a,b = (int(x) for x in lines[_+D+1].split())
    SickPeople[_]= [a,b]

for _ in range(D):
    People.append([])
    a,b,c = (int(x) for x in lines[_+1].split())
    People[_]= [a,b,c]

for _ in range(S):
    Possible.append(set())
    for e in range(D):
        if People[e][0] == SickPeople[_][0]:
            if People[e][2] < SickPeople[_][1]:
                Possible[_].add(People[e][1])
SicknessList = []
I = list(set.intersection(*Possible))
for _ in range(len(I)):
    Sickness = set()
    for e in range(D):
        if I[_] == People[e][1]:
            Sickness.add(People[e][0])
    SicknessList.append(len(Sickness))

Doses = max(SicknessList)
        

with open("badmilk.out", 'w') as fOutput:
    fOutput.write(str(Doses))


