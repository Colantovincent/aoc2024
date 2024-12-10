from collections import Counter
def orderFileSystem(diskMap):
    def isEven(element):
        return element % 2 == 0
    lunghezza = len(diskMap)
    orderedDiskMap = []
    currId = 0
    for i in range(lunghezza):
        if isEven(i):
            for j in range(int(diskMap[i])):
                orderedDiskMap.append(str(currId))
            currId += 1
        else:
            for j in range(int(diskMap[i])):
                orderedDiskMap.append(".")
    #ordiniamo la lista
    lunghezzaHDD = len(orderedDiskMap)
    countedFiles = Counter(orderedDiskMap)
    numFile = lunghezzaHDD - countedFiles["."]
    for i in range(numFile):
        if orderedDiskMap[i] == ".":
            for j in range(lunghezzaHDD - 1, -1, -1):
                if orderedDiskMap[j] != ".":
                    #print(orderedDiskMap)
                    orderedDiskMap[i], orderedDiskMap[j] = orderedDiskMap[j], orderedDiskMap[i]
                    break
    #contiamo la checksum
    checksum = 0
    for i in range(numFile):
        checksum += int(orderedDiskMap[i]) * i
    print(orderedDiskMap)
    return checksum
def unfragmentedOrdering(diskMap):
    def diskToList(disk):
        result = []
        for file in disk:
            fileId, fileSize = file
            if fileId is None:
                fileId = "."
            for i in range(fileSize):
                result.append(fileId)
        return result
    def getNewPlacement(fileSize, maxIndex, disk):
        #Controlla tutti i segmenti aggregati compresi tra 0 e maxIndex
        for i, entry in enumerate(disk):
            if i > maxIndex:
                break
            currFileId, currSize = entry
            #Se trova un segmento di lunghezza maggiore che non contenga "dati", lo returna
            if currFileId is None and currSize >= fileSize:
                return (i, currSize)
        return (None, None)
    diskStructure = []
    encriptedSize = len(diskMap)
    currId = 0
    for i in range(encriptedSize):
        if i % 2 == 0:
            file_id = currId
            currId += 1
        else:
            file_id = None
        diskStructure.append((file_id, int(diskMap[i])))
    i = len(diskStructure) - 1
    while i >= 0:
        fileId, fileSize = diskStructure[i]
        #Per ogni fileId non vuoto (usiamo None per rappresentare la memoria libera invece di ".") chiamiamo la funzione per trovare il segmento vuoto più "a sinistra"
        if fileId is not None:
            destI, freeSpace = getNewPlacement(fileSize, i, diskStructure)
            
            if destI is not None:
                #Cambia il valore in posizione destI con il file attualmente in analisi
                diskStructure[destI], diskStructure[i] = diskStructure[i], (None, fileSize) 
                currFreeSpace = freeSpace - fileSize
                #skippa gli spazi liberi lunghi 0
                if currFreeSpace > 0:
                    newFreeSpace = (None, currFreeSpace)
                    diskStructure.insert(destI + 1, newFreeSpace)
                    i += 1
        i -= 1
    return sum(i * val for i, val in enumerate(diskToList(diskStructure)) if val != ".")
with open("input.txt", "r") as F:
    cryptedDisk = F.read()
print(unfragmentedOrdering(cryptedDisk))