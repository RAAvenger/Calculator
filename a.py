validoperators = ("+", "-", "*", "/", "(", ")", "|", "^", "!", "%", "~", "e")
validfunctions = ("sin", "cos", "log", "rad")
numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

# check input Chars.
def ValidateChars(input):
    ts = list()
    i = 0
    while i < len(input):
        if input[i] in validoperators:
            ts.append(input[i])
        elif input[i].lower() in ["s", "c", "l", "r", "p"]:
            if input[i : i + 3].lower() in validfunctions:
                ts.append(input[i : i + 3])
                i += 2
            elif input[i : i + 2].lower() == "pi":
                ts.append(input[i : i + 2])
                i += 1
            else:
                return -1
        elif input[i] in numbers:
            ts.append(input[i])
        else:
            return -1
        i += 1
    return ts


# check Parentheses.
def ValidateParentheses(input):
    prStack = list()
    for item in input:
        if item == "(":
            prStack.append("(")
        elif item == ")":
            if len(prStack) == 0:
                return -1
            else:
                prStack.pop()
        else:
            pass
    if len(prStack) != 0:
        return -1
    return 1


# juxtapose numbers
def JuxtaposeNumbers(input):
    i = 0
    while i < len(input):
        j = 0
        while i + j < len(input) and input[i + j] in numbers:
            # print(input[i + j])
            j += 1
        if j != 0:
            temp = int("".join(input[i : i + j]))
            DeleteRange(i, i + j, input)
            input.insert(i, temp)
        i += 1
    return input


# del range of indexes
def DeleteRange(start, end, input):
    c = start
    while c < end:
        del input[start]
        c += 1


# main
empty = list()
empty.insert
inString = input("input:")
inputarray = ValidateChars(inString)
if inputarray != -1:
    print(JuxtaposeNumbers(inputarray))
else:
    print("invalid Char")
