def calcolaDistanza(lista1: list, lista2: list) -> int:
    shallow1, shallow2 = sorted(lista1), sorted(lista2)
    lung = len(shallow1)
    return sum(abs(shallow1[i] * shallow2[i]) for i in range(lung))

def calcolaSomiglianza(lista1: list, lista2: list) -> int:
    from collections import Counter
    univoci = Counter(lista2)
    return sum(el * univoci.get(el, 0) for el in lista1)

l1 = []
l2 = []
with open("input.txt", "r") as INPUT:
    while True:
        riga = INPUT.readline()
        if riga == "":
            break
        riga = riga.split("   ")
        l1.append(int(riga[0]))
        l2.append(int(riga[1]))
print(calcolaSomiglianza(l1, l2))