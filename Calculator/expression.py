import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Calculator.validation import FindCloseBracketIndex, FindBlockes


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
        self.term = []
        error = self.SetTerm(term)
        if error:
            print(error)

    def __str__(self):
        result = []
        for item in self.term:
            result.append(item.__str__())
        return str(result).replace("\\", "")

    def UseUnaryOperators(self, operator, operand1, operand2=10):
        """
        Use unary operators on operand(s) and calculate result.
        """
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

    def UseBinaryOperators(self, operator, number1, number2=10):
        """
        Use binary operators on operands and calculate result.
        """
        if operator == "+":
            return number1 + number2
        if operator == "-":
            return number1 + number2
        if operator == "*":
            return number1 + number2
        if operator == "/":
            return number1 + number2
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
        get term list and if it has operators with different priority create Expressions for higher priority terms. 
        """
        if not term:
            return "empty input"
        t = FindBlockes(0, len(term), term)

        # thisPriority = 0
        # newPriority = 0
        # i = 0
        # ## Index = -1 means "not set".
        # pIndex = -1
        # startIndex = -1
        # while i < len(term):
        #     if term[i] in ["("] and i + 2 < len(term) and term[i + 2] != ")":
        #         ## handle Parentheses.
        #         closeBracketIndex = FindCloseBracketIndex(i, term)
        #         self.term.append(Expression(term[i + 1 : closeBracketIndex]))
        #         i = closeBracketIndex + 1
        #         continue
        #     if type(term[i]) in [int, float, type(Expression)]:
        #         pass
        #     elif term[i] in self.priority1BinaryOperators:
        #         newPriority = 1
        #     elif term[i] in self.priority2BinaryOperators:
        #         newPriority = 2
        #     elif term[i] in self.priority3BinaryOperators:
        #         newPriority = 3
        #     elif term[i] in self.priority4BinaryOperators:
        #         newPriority = 4
        #     if startIndex == -1:
        #         ## A "thisPriority < newPriority" condition not apend.
        #         if thisPriority == 0:
        #             ## initial mode.
        #             thisPriority = newPriority
        #             self.term.append(term[i])
        #         elif thisPriority < newPriority:
        #             ## start of a higher priority term.
        #             if type(term[i - 1]) == int:
        #                 ## ex: "...num*num..." or "...num^num..." or ... .
        #                 startIndex = i - 1
        #                 self.term.pop()
        #             else:
        #                 ## ex: "...num+(num..." or "...num/(num..." or ... .
        #                 startIndex = i
        #         elif thisPriority > newPriority:
        #             ## new priority is lower then befor so we create a Expression for start of term until here.
        #             if thisPriority != 5:
        #                 newTerm = Expression(self.term)
        #                 self.term.clear()
        #                 self.term.append(newTerm)
        #             self.term.append(term[i])
        #             thisPriority = newPriority
        #         else:
        #             ## term[i] is a number or unary Operator or function
        #             self.term.append(term[i])
        #     else:
        #         ## A "thisPriority < newPriority" condition apend befor and we are counting a "higher priority term" length.
        #         if i == len(term) - 1:
        #             newTerm = Expression(term[startIndex : i + 1])
        #             self.term.append(newTerm)
        #         elif thisPriority == newPriority:
        #             ## end of higher priority, back to previous priority.
        #             ## so we create a Expression for high priority term.
        #             self.term.append(Expression(term[startIndex:i]))
        #             self.term.append(term[i])
        #             startIndex = -1
        #         elif thisPriority > newPriority:
        #             ## end of higher priority, goiing to lower priority then previous priority.
        #             ## so we create a Expression for high priority term and other one for start of term until here.
        #             newTerm = Expression(term[startIndex:i])
        #             self.term.append(newTerm)
        #             newTerm = Expression(self.term)
        #             self.term.clear()
        #             self.term.append(newTerm)
        #             self.term.append(term[i])
        #             thisPriority = newPriority
        #             startIndex = -1
        #     i += 1
        # self.term = self.RemoveAll(self.term, ")", "(")
