import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Calculator.expression import Expression
import Calculator.validation

# inString = input("input:")
inString = [
    # "1+2",
    # "1+2*3+8",
    # "1+2+3*4*5^6*log(7)",
    # "1*2+3*4*5-6",
    # "(1+2)*3*4+5",
    # "1%2^3*4^5+7*8",
    # "(10+12+15+(19*20))",
    "(1*2)^(3+4)-5%6/log(11)*~(log(12)*2!)"
]
resultString = [
    # "[1+2]",
    # "[1+[2*3]+8]",
    # "[1+2+[3*4*[5^6]*log7]]",
    # "[[1*2]+[3*4*5]-6]",
    # "[[[1+2]*3*4]+5]",
    # "[[[[1%2]^3]*[4^5]]+[7*8]]",
    # "[[10+12+15+[19*20]]]",
    "[[[1*2]^[3+4]]-[[5%6]/log11*~[log12*2!]]]"
]
for i in range(len(inString)):
    inputTerm, error = Calculator.validation.FullValidate(inString[i])
    if not error:
        result = Expression(inputTerm)
        stringRes = str(result).replace("'", "")
        stringRes = str(stringRes).replace(" ", "")
        stringRes = str(stringRes).replace('"', "")
        stringRes = str(stringRes).replace(",", "")
        print(stringRes)
        # if stringRes == resultString[i]:
        #     print("correct")
        # else:
        #     print("not match:")
        #     print(resultString[i])
        # print("____________________________________________________________")
    else:
        print(error)
