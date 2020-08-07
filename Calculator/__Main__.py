import math
import Calculator.validation

## main
inString = input("input:")
result = validation.FullValidate(inString)
if result[0] != -1:
    equation = result[1]
    print(equation)
    # RecursiveCalculate(0, len(equation), equation)
else:
    ErroR = result[1]
    print(ErroR)
