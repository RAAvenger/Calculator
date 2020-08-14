import math
import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from Calculator.validation import FindCloseBracketIndex, FindBlockes, DeleteRange


class Expression:
    priority1BinaryOperators = ["+", "-"]
    priority2BinaryOperators = ["*", "/"]
    priority3BinaryOperators = ["^"]
    priority4BinaryOperators = ["%"]
    functions = ["sin", "cos", "log", "sqrt"]
    prefixUnaryOperators = ["~"]
    pastfixUnaryOperators = ["!"]

    def __init__(self, term):
        # term keeps operands and operators with same priority.
        self.input = []
        self.stack = []
        error = self.SetTerm(term)
        if error:
            print(error)

    def __str__(self):
        result = []
        for item in self.input:
            result.append(item.__str__())
        return str(result).replace("\\", "")

    def UseUnaryOperators(self, operator, operand1, operand2=10):
        """
        Use unary operators on operand(s) and calculate result.
        """
        if type(operand1) == Expression:
            ## get expression result.
            operand1 = operand1.CalculateResult()
        if operator == "sin":
            return math.sin(operand1)
        elif operator == "cos":
            return math.cos(operand1)
        elif operator == "log":
            return math.log(operand1, operand2)
        elif operator == "sqrt":
            return math.sqrt(operand1)
        elif operator == "~":
            return operand1 * -1
        elif operator == "!":
            return math.factorial(operand1)

    def UseBinaryOperators(self, operator, number1, number2=10):
        """
        Use binary operators on operands and calculate result.
        """
        if operator == "+":
            return number1 + number2
        if operator == "-":
            return number1 - number2
        if operator == "*":
            return number1 * number2
        if operator == "/":
            return number1 / number2
        if operator == "%":
            return number1 % number2
        if operator == "^":
            return math.pow(number1, number2)

    def RemoveAll(self, inputList, *chars):
        """
        Remove All chars from inputList.
        """
        for i in reversed(range(len(inputList))):
            if inputList[i] in chars:
                inputList.pop(i)
        return inputList

    def SetTerm(self, term):
        """
        create a Prefix expression from term( an infix expression ).
        """
        if not term:
            return "empty input"
        ## find blockes and create a new Expression for each one of them.
        blockes = FindBlockes(0, len(term), term)
        for blockRange in reversed(blockes):
            if blockRange[1] - blockRange[0] != 2:
                blockExpression = Expression(term[blockRange[0] + 1 : blockRange[1]])
                DeleteRange(blockRange[0] + 1, blockRange[1], term)
                term.insert(blockRange[0], blockExpression)
        term = self.RemoveAll(term, ")", "(")
        self.input = term
        ## calculate and get result of all Unary Operations in expression.
        for i in reversed(range(len(term))):
            if term[i] in self.pastfixUnaryOperators:
                term[i - 1] = self.UseUnaryOperators(term[i], term[i - 1])
                term.pop(i)
            elif term[i] in self.prefixUnaryOperators + self.functions:
                term[i] = self.UseUnaryOperators(term[i], term[i + 1])
                term.pop(i + 1)
        ## create Prefix expression.
        priorities = []
        for item in term:
            priorities.append(self.FindPriority(item))
        expressionStack = []
        i = 0
        j = -1
        while i < len(term):
            if i == 0:
                expressionStack.append(term[i])
            elif priorities[i] < priorities[j]:
                tempStack = []
                while priorities[i] < priorities[j] and j >= 0:
                    tempStack.append(expressionStack.pop())
                    j -= 1
                expressionStack.append(term[i])
                for item in reversed(tempStack):
                    expressionStack.append(item)
            else:
                expressionStack.append(term[i])
            i += 1
            j = i - 1
        self.stack = expressionStack

    def CalculateResult(self):
        """
        calculate expression result using preorder expression in stack.
        """
        expressionStack = self.stack.copy()
        for i in reversed(range(len(expressionStack))):
            if (
                expressionStack[i]
                in self.priority1BinaryOperators
                + self.priority2BinaryOperators
                + self.priority3BinaryOperators
                + self.priority4BinaryOperators
            ):
                expressionStack[i] = self.UseBinaryOperators(
                    expressionStack[i], expressionStack[i + 1], expressionStack[i + 2]
                )
                expressionStack.pop(i + 2)
                expressionStack.pop(i + 1)
            elif type(expressionStack[i]) == Expression:
                expressionStack[i] = expressionStack[i].CalculateResult()
        return expressionStack[0]

    def FindPriority(self, theInput):
        """
        get operand or operator and return its priority.
        """
        if (
            type(theInput) in [int, float, Expression]
            or theInput
            in self.functions + self.pastfixUnaryOperators + self.prefixUnaryOperators
        ):
            return 5
        elif theInput in self.priority4BinaryOperators:
            return 4
        elif theInput in self.priority3BinaryOperators:
            return 3
        elif theInput in self.priority2BinaryOperators:
            return 2
        elif theInput in self.priority1BinaryOperators:
            return 1

