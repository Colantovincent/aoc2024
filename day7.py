def isOperationValid(equalsTo: int, elements: list) -> bool:
    def getPossibleResults(numbers: list) -> set:
        possibleResults = {numbers[0]}
        numOperations = len(numbers)
        for i in range(1, numOperations):
            currentResults = set()
            for result in possibleResults:
                currentSum = result + numbers[i]
                currentMultiplication = result * numbers[i]
                currentResults.add(currentSum)
                currentResults.add(currentMultiplication)
            possibleResults = currentResults
        return possibleResults
    possibleResults = getPossibleResults(elements)
    return equalsTo in possibleResults
def isOperationValid2(equalsTo: int, elements: list) -> bool:
    def getPossibleResults(numbers: list) -> set:
        possibleResults = {numbers[0]}
        numOperations = len(numbers)
        for i in range(1, numOperations):
            currentResults = set()
            for result in possibleResults:
                currentSum = result + numbers[i]
                currentMultiplication = result * numbers[i]
                currentConcatenation = int(str(result) + str(numbers[i]))
                currentResults.add(currentSum)
                currentResults.add(currentMultiplication)
                currentResults.add(currentConcatenation)
            possibleResults = currentResults
        return possibleResults
    possibleResults = getPossibleResults(elements)
    return equalsTo in possibleResults
with open("input.txt", "r") as F:
    validSum = 0
    while True:
        operation = F.readline().rstrip("\n")
        if operation == "":
            break
        operation = operation.split(":")
        result = int(operation[0])
        operationMembers = []
        for el in operation[1].split():
            operationMembers.append(int(el))
        if isOperationValid2(result, operationMembers):
            validSum += result
print(validSum)