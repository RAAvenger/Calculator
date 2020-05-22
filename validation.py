validSingleChars = ("e", "+", "-", "*", "/", "(", ")", "|", "^", "!", "%", "~")
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


## check char order.
def ValidateOrder(inputList):
    i = 0
    ## "binary" operators at start or "unary or binary" operators at end of list. ex: "+...", "...+", "...sin"
    if (inputList[0] != "~" and inputList[0] in validSingleChars) or (
        inputList[-1] in validSingleChars + validMultiChaer
    ):
        return -1
    while i < len(inputList) - 1:
        ## a function without parenthes after it. ex: "sin12".
        if inputList[i] in validMultiChaer and inputList[i + 1] != "(":
            return -1
        ## "number" befor "open parenthes" or "number or unary operator" after "close parenthes". ex: "2(", ")2", ")sin".
        if (
            inputList[i] == ")" and (inputList[i + 1] in numbers + validMultiChaer)
        ) or (inputList[i] in numbers and inputList[i + 1] == "("):
            return -1
        ## empty parentheses. ex: "()".
        if inputList[i] == "(" and inputList[i + 1] == ")":
            return -1


## juxtapose numbers(convert string numbers to int).
def JuxtaposeNumbers(inputString):
    i = 0
    while i < len(inputString):
        if inputString[i] == "pi":
            inputString[i] = math.pi
        elif inputString[i] == "e":
            inputString[i] = math.e
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


## get start, end and list then return list of start and end indexes of all blockes.
def FindBlockes(start, end, inputList):
    result = list()
    while start < end:
        if inputList[start] == "(":
            closeBracketIndex = FindCloseBracketIndex(start, inputList)
            result.append([start, closeBracketIndex])
            start = closeBracketIndex
        start += 1
    return result
