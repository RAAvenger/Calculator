import math

validSingleChars = ["e", "+", "-", "*", "/", "(", ")", "^", "!", "%", "~"]
validMultiChars = ["pi", "sin", "cos", "log", "sqrt"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
binaryOperators = ["+", "-", "*", "/", "^", "%"]
functions = ["sin", "cos", "log", "sqrt"]
prefixUnaryOperators = ["~"]
pastfixUnaryOperators = ["!"]

## check input Chars and convert string to list.
def ValidateChars(inputString):
    equationList = list()
    i = 0
    while i < len(inputString):
        if inputString[i] in validSingleChars:
            equationList.append(inputString[i])
        elif inputString[i] in ["s", "c", "l", "p"]:
            if inputString[i : i + 2] in validMultiChars:
                equationList.append(inputString[i : i + 2])
                i += 1
            elif inputString[i : i + 3] in validMultiChars:
                equationList.append(inputString[i : i + 3])
                i += 2
            elif inputString[i : i + 4] in validMultiChars:
                equationList.append(inputString[i : i + 4])
                i += 3
            else:
                return -1
        elif inputString[i] in numbers:
            equationList.append(inputString[i])
        else:
            return -1
        i += 1
    return equationList


## check Parentheses.
def ValidateParentheses(inputString):
    parenthesesStack = list()
    for item in inputString:
        if item == "(":
            parenthesesStack.append("(")
        elif item == ")":
            if len(parenthesesStack) == 0:
                return -1
            else:
                parenthesesStack.pop()
    if len(parenthesesStack) != 0:
        return -1
    return 1


## check char order.
def ValidateOrder(inputList):
    i = 0
    ## ""binary or pastfix Unary" Operators" at start or "function or "prefix Unary or binary" operators" at end of list. ex: "+...", "!...", "...+", "...sin"
    if (
        inputList[0] in binaryOperators + pastfixUnaryOperators
        or inputList[-1] in functions + prefixUnaryOperators + binaryOperators
    ):
        return -1
    while i <= len(inputList) - 2:
        ## a function without parenthes after it. ex: "sin12".
        if inputList[i] in functions and inputList[i + 1] != "(":
            return -1
        ## "number or pastfix Unary Operators" befor "open parenthes" or "number or function or prefix Unary operators" after "close parenthes". ex: "2(", ")2", ")sin".
        if (
            inputList[i] in numbers + pastfixUnaryOperators and inputList[i + 1] == "("
        ) or (
            inputList[i] == ")"
            and (inputList[i + 1] in numbers + functions + prefixUnaryOperators)
        ):
            return -1
        ## empty parentheses. ex: "()".
        if inputList[i] == "(" and inputList[i + 1] == ")":
            return -1
        ## binary or Unary operator without operand. ex: "1++2", "1~+2", "1+!2", "...!1", "1~...".
        if (
            (
                inputList[i] in binaryOperators + prefixUnaryOperators
                and inputList[i + 1] in binaryOperators + pastfixUnaryOperators
            )
            or (
                inputList[i] in pastfixUnaryOperators
                and type(inputList[i + 1]) in (int, float)
            )
            or (
                type(inputList[i]) in (int, float)
                and inputList[i + 1] in prefixUnaryOperators
            )
        ):
            return -1
        ## operands without operator or no operator between number and function. ex: "...1pi...", "...e1...", "2sin".
        if (
            type(inputList[i]) in (int, float)
            and type(inputList[i + 1]) in (int, float)
        ) or (type(inputList[i]) in (int, float) and (inputList[i + 1] in functions)):
            return -1
        i += 1
    return 1


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


def FullValidate(inputString):
    equationList = ValidateChars(inputString.lower())
    if equationList != -1:
        if ValidateParentheses(equationList) != -1:
            equationList = JuxtaposeNumbers(equationList)
            if ValidateOrder(equationList) != -1:
                return (1, equationList)
            else:
                return (-1, "order is not valid")
        else:
            return (-1, "parentheses are not valid")
    else:
        return (-1, "chars are not valid")


## test main
inputString = input("input:")
result = FullValidate(inputString)
if result[0] != -1:
    equation = result[1]
    print(equation)
else:
    ErroR = result[1]
    print(ErroR)