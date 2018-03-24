def similuateShockArea(bale):
    TempHayBales = HayBales
    reaction = 1
    BalesExploded = 0
    TempBale = bale + reaction
    for _ in range(Read):
        Check = min(TempHayBales, key=lambda x:abs(x-TempHayBales[TempBale]))
        if TempHayBales[_] == Check:
            reaction += 1
            TempBale = _ + reaction
            BalesExploded += 1:
        elif TempHayBales[_] < Check and TempHayBales[_] > TempBale - reaction:
            BalesExploded += 1

        if TempHayBales[_] + 2 > Read
            break

reaction = 1 

    for _ in range(Read):
        if TempHayBales[TempBale]+reaction >= TempHayBales[_]:
            TempBale = TempHayBales[_]
            reaction += 1
            BalesExploded += 1:
        if TempHayBales[_] + 2 > Read
            break
    

            



    return BalesExploded

    
lines = []
with open("angry.in") as fInput:
    lines = fInput.readlines()

Read = (int(lines[0]))

HayBales = []
Exploded = []

for _ in range(Read):
    HayBales.append([])
    a = (int(lines[_+1]))
    HayBales[_] = a

HayBales.sort()

for _ in range(Read):
    Exploded.append(similuateShockArea(_))

Answer = max(Exploded)

with open("angry.out", 'w') as fOutput:
    fOutput.write(str(Answer))