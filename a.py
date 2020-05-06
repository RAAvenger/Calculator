import math

validSingleChars = ("+", "-", "*", "/", "(", ")", "|", "^", "!", "%", "~", "e")
validMultiChaer = ("pi", "sin", "cos", "log", "sqrt")
numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

## check input Chars.
def ValidateChars(input):
    ts = list()
    i = 0
    while i < len(input):
        if input[i] in validSingleChars:
            ts.append(input[i])
        elif input[i] in ["s", "c", "l", "p"]:
            if input[i : i + 2] in validMultiChaer:
                ts.append(input[i : i + 2])
                i += 1
            elif input[i : i + 3] in validMultiChaer:
                ts.append(input[i : i + 3])
                i += 2
            elif input[i : i + 4] in validMultiChaer:
                ts.append(input[i : i + 4])
                i += 3
            else:
                return -1
        elif input[i] in numbers:
            ts.append(input[i])
        else:
            return -1
        i += 1
    return ts


## check Parentheses.
def ValidateParentheses(inputString):
    prStack = list()
    for item in inputString:
        if item == "(":
            prStack.append("(")
        elif item == ")":
            if len(prStack) == 0:
                return -1
            else:
                prStack.pop()
    if len(prStack) != 0:
        return -1
    return 1


## juxtapose numbers(convert string numbers to int).
def JuxtaposeNumbers(inputString):
    i = 0
    while i < len(inputString):
        j = 0
        while i + j < len(inputString) and inputString[i + j] in numbers:
            # print(input[i + j])
            j += 1
        if j != 0:
            temp = int("".join(inputString[i : i + j]))
            DeleteRange(i, i + j, inputString)
            inputString.insert(i, temp)
        i += 1
    return inputString


## del range of indexes.
def DeleteRange(start, end, inputList):
    c = start
    while c < end:
        del inputList[start]
        c += 1


## unary operators.
def UseUnaryOperators(operator, number1, number2=10):
    if operator == "sin":
        return math.sin(number1)
    elif operator == "cos":
        return math.cos(number1)
    elif operator == "log":
        return math.log(number1, number2)
    elif operator == "sqrt":
        return math.sqrt(number1)
    elif operator == "~":
        return number1 * -1


## find index of close Bracket of given open bracket's index.
def FindCloseBracketIndex(openBracketIndex, inputList):
    prStack = list()
    i = openBracketIndex
    while i < len(inputList):
        if inputList[i] == "(":
            prStack.append("(")
        elif inputList[i] == ")":
            prStack.pop()
            if len(prStack) == 0:
                return int(i)

        i += 1


def FindBlockes(start, end, inputList):
    result = list()
    while start < end:
        if inputList[start] == "(":
            closeBracketIndex = FindCloseBracketIndex(start, inputList)
            result.append([start, closeBracketIndex])
            start = closeBracketIndex
        start += 1
    return result


## main recursive calculate finction
def Calculate(start, end, inputList):
    print(inputList[start:end])
    blockIndexes = FindBlockes(start, end, inputarray)
    if blockIndexes.count != 0:
        for item in blockIndexes:
            Calculate(item[0] + 1, item[1], inputList)


## main
empty = list()
empty.insert
inString = input("input:")
inputarray = ValidateChars(inString.lower())
if inputarray != -1 and ValidateParentheses(inputarray)!=-1:
    JuxtaposeNumbers(inputarray)
    Calculate(0, len(inputarray), inputarray)
    # print(inputarray)
else:
    print("invalid Char")
