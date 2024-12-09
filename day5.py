def generaGrafo(regole):
    #rimuove coppie di duplicati per sicurezza
    uniqueRules = set()
    for el in regole:
        uniqueRules.add(tuple(el.split("|")))
    #genera un dizionario dove le chiavi sono i primi elementi in ogni regola e gli da come elemento una lista di tutti i numeri di pagina che dovrebbero comparirvi dopo 
    rulesGraph = {}
    for rule in uniqueRules:
        if rule[0] in rulesGraph:
            rulesGraph[rule[0]].append(rule[1])
        else:
            rulesGraph[rule[0]] = [rule[1]]
    return rulesGraph
def isOrdered(pagesPrinted):
    for i in range(len(pagesPrinted) - 1):
        curr_page = pagesPrinted[i]
        next_page = pagesPrinted[i + 1]
        if next_page in rulesGraph:
            if curr_page in rulesGraph[next_page]:
                return False
    return True
def ordinaLista(pagesPrinted):
    # Keep sorting until the list is in order
    while not isOrdered(pagesPrinted):
        for i in range(len(pagesPrinted) - 1):
            curr_page = pagesPrinted[i]
            next_page = pagesPrinted[i + 1]
            if next_page in rulesGraph:
                if curr_page in rulesGraph[next_page]:
                    # Swap the elements to try and get closer to ordering
                    pagesPrinted[i], pagesPrinted[i + 1] = next_page, curr_page
rules = []
with open("input.txt", "r") as F:
    line = F.readline().rstrip("\n")
    while line != "":
        rules.append(line)
        line = F.readline().rstrip("\n")
    printedOrder = []
    line = F.readline().rstrip("\n")
    while line != "":
        printedOrder.append(line.split(","))
        line = F.readline().rstrip("\n")
rulesGraph = generaGrafo(rules)
sommaOrd = 0
sommaNonOrd = 0
listaOro = []
for pageList in printedOrder:
    if isOrdered(pageList):
        sommaOrd += int(pageList[(len(pageList) // 2)])
    else:
        ordinaLista(pageList)
        sommaNonOrd += int(pageList[(len(pageList) // 2)])
print(sommaOrd, sommaNonOrd)