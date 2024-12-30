#No input parsing cuz it was faster here to just copy the small input from the website
A, B, C = 2024, 0, 0
PROGRAM = [0, 3, 5, 4, 3, 0]
# helpers
def adv(comboOperand, aVal):
    return int(aVal / 2 ** comboOperand)

def bxl(literalOperand, bVal):
    return bVal ^ literalOperand

def bst(comboOperand):
    return comboOperand % 8

# No jnz

def bxc(bVal, cVal):
    return bVal ^ cVal

def out(comboOperand):
    return comboOperand % 8

def bdv(comboOperand, aVal):
    return int(aVal / 2 ** comboOperand)

def cdv(comboOperand, aVal):
    return int(aVal / 2 ** comboOperand)

def eval(aVal, bVal, cVal, i, program):
    COMBOVALS = {4: aVal, 5: bVal, 6: cVal}
    opcode = program[i]
    arg = program[i + 1]
    comb = COMBOVALS.get(arg, arg)
    # Return the value to add to the output list, aVal, bVal, cVal, and the updated instruction pointer
    if opcode == 0:
        aVal = adv(comb, aVal)
        return (None, aVal, bVal, cVal, i + 2)
    elif opcode == 1:
        bVal = bxl(arg, bVal)
        return (None, aVal, bVal, cVal, i + 2)
    elif opcode == 2:
        bVal = bst(comb)
        return (None, aVal, bVal, cVal, i + 2)
    elif opcode == 3:
        if aVal == 0:
            return (None, aVal, bVal, cVal, i + 2)
        else:
            return (None, aVal, bVal, cVal, arg)
    elif opcode == 4:
        bVal = bxc(bVal, cVal)
        return (None, aVal, bVal, cVal, i + 2)
    elif opcode == 5:
        outVal = out(comb)
        return (outVal, aVal, bVal, cVal, i + 2)
    elif opcode == 6:
        bVal = bdv(comb, aVal)
        return (None, aVal, bVal, cVal, i + 2)
    elif opcode == 7:
        cVal = cdv(comb, aVal)
        return (None, aVal, bVal, cVal, i + 2)

def runProgram(aVal, bVal, cVal, program):
    i = 0
    res = []
    lung = len(program) - 1
    while i < lung:
        (out, aVal, bVal, cVal, i) = eval(aVal, bVal, cVal, i, program)
        if out is not None:
            res.append(out)
    return res

def findSmallestA(program, currPos, currDigit):
    #L'output è basato su un numero ottale
    for i in range(8):
        #Per ogni numero ottale, lo converto e se la sequenza ottenuta è uguale alla sequenza in PROGRAM dalla posizione attuale fino alla fine, prendo e porto a casa
        if runProgram(currDigit * 8 + i, 0, 0, program) == program[currPos:]:
            if currPos == 0:
                #returna il valore finale se siamo arrivati a una sequenza completamente uguale
                return currDigit * 8 + i
            found = findSmallestA(program, currPos - 1, currDigit * 8 + i)
            if found is not None:
                return found
    return None

#DFS che parte dall'ultima cifra del valore obiettivo e itera finché non trova un valore
print(findSmallestA(PROGRAM, len(PROGRAM) - 1, 0))

#parte 1
print(runProgram(A, B, C, PROGRAM))