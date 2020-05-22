import math
import validation

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


## main recursive calculate finction
def Calculate(start, end, inputList):
    print(inputList[start:end])
    blockIndexes = validation.FindBlockes(start, end, inputarray)
    if blockIndexes.count != 0:
        for item in blockIndexes:
            Calculate(item[0] + 1, item[1], inputList)


## main
inString = input("input:")
inputarray = validation.ValidateChars(inString.lower())
if inputarray != -1 and validation.ValidateParentheses(inputarray) != -1:
    validation.JuxtaposeNumbers(inputarray)
    if validation.ValidateOrder(inputarray) != -1:
        Calculate(0, len(inputarray), inputarray)
    else:
        print("wrong order!")
    # print(inputarray)
else:
    print("invalid Char!")
