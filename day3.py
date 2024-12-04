
import re
def cleanseMemory(corruptedMem):
    matchedNums = re.findall(mulPattern, corruptedMem)
    return sum((int(firstEl) * int(secondEl)) for firstEl, secondEl in matchedNums)
def advC(corruptedMem):
    mul_enabled = True
    totale = 0
    segmenti = re.split(r"(\bdo\(\)|\bdon\'t\(\))", corruptedMem)
    for segmento in segmenti:
        #reintegra la parentesi che si è "mangiata" la funzione split
        segmento += ")"
        if 'do()' in segmento:
            mul_enabled = True
        elif 'don\'t()' in segmento:
            mul_enabled = False
        if mul_enabled:
            totale += cleanseMemory(segmento)
    
    return totale

with open("input.txt") as F:
    corruptedData = F.read()
mulPattern = r"mul\((\d{1,3}),(\d{1,3})\)"
print(advC(corruptedData))