def calcolaReattore(valori: list) -> int:
    lung = len(valori)
    crescente = True
    decrescente = True
    for i in range(lung - 1):
        #prende il valore in modulo per vedere quanto distano gli elementi, poi controlla che la lista sia decrescente o crescente
        diff = abs(valori[i] - valori[i + 1])
        if diff < 1 or diff > 3:
            return 0
        if valori[i] < valori[i + 1]:
            decrescente = False 
        elif valori[i] > valori[i + 1]:
            crescente = False
    #se sia decrescente che crescente sono False, returna 0
    if crescente or decrescente:
        return 1
    return 0
def calcolaReattoreDampener(report: list) -> int:
    if calcolaReattore(report) == 1:
        return 1
    for i in range(len(report)):
        #list slicing per rimuovere un elemento dalla lista
        dampenedReport = report[:i] + report[i+1:]
        if calcolaReattore(dampenedReport) == 1:
            return 1    
    return 0
counter = 0
with open("input.txt", "r") as F:
    testo = F.read().splitlines()
    for riga in testo:
        riga = riga.split(" ")
        print("\n" + str(riga))
        interi = list(map(int, riga))
        counter += calcolaReattore(interi) #oppure counter += calcolaReattoreDampener(interi)
print(counter)