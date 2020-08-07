class expression:
    priority1BinaryOperators = ["+", "-"]
    priority2BinaryOperators = ["*", "/"]
    priority3BinaryOperators = ["^"]
    priority4BinaryOperators = ["%"]
    functions = ["sin", "cos", "log", "sqrt"]
    prefixUnaryOperators = ["~"]
    pastfixUnaryOperators = ["!"]

    def Expression(self, term):
        # term keeps operands and operators with same priority.
        self.term = []
        error = self.SetTerm(term)
        if error:
            print(error)
            exit()

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

    def cleanParentheses(self):
        """
        Remove All Parentheses.
        """
        for i in len(self.term) - range(len(self.term)):
            if self.term(i) in ["(", ")"]:
                self.term.pop(i)

    def SetTerm(self, term):
        """
        get term list and if it has operators with different priority create Expressions for higher priority terms. 
        """
        if not term:
            return "empty input"
        thisPriority = 0
        newPriority = 0
        i = 0
        ## startIndex = -1 means start not set.
        startIndex = -1
        while i < len(term):
            if type(term[i]) == int:
                pass
            elif term[i] in self.priority1BinaryOperators:
                newPriority = 1
            elif term[i] in self.priority2BinaryOperators:
                newPriority = 2
            elif term[i] in self.priority3BinaryOperators:
                newPriority = 3
            elif term[i] in self.priority4BinaryOperators:
                newPriority = 4
            elif term[i] == "(":
                newPriority = 5
            if startIndex == -1:
                ## A "thisPriority < newPriority" condition not apend.
                if thisPriority == 0:
                    ## initial mode.
                    thisPriority = newPriority
                    self.term.append(term[i])
                elif thisPriority < newPriority:
                    ## start of a higher priority term.
                    if (
                        term[i - 1] in self.functions + self.prefixUnaryOperators
                        or type(term[i - 1]) == int
                    ):
                        ## ex: "...log(..." or ".../..." or ... .
                        startIndex = i - 1
                    else:
                        ## ex: "...+(..." or ".../..." or ... .
                        startIndex = i
                elif thisPriority > newPriority:
                    ## new priority is lower then befor so we create a Expression for start of term until here.
                    newTerm = Exception(self.term)
                    self.term.clear()
                    self.term.append(newTerm)
                    self.term.append(term[i])
                    thisPriority = newPriority
                else:
                    ## term[i] is a number or unary Operator or function
                    self.term.append(term[i])
            else:
                ## A "thisPriority < newPriority" condition apend befor and we are counting a "higher priority term" length.
                if thisPriority == newPriority or i == len(term) - 1:
                    ## end of higher priority, back to previous priority.
                    ## so we create a Expression for high priority term.
                    newTerm = Exception(term[startIndex:i])
                    self.term.append(newTerm)
                    self.term.append(term[i])
                    startIndex = -1
                elif thisPriority > newPriority:
                    ## end of higher priority, goiing to lower priority then previous priority.
                    ## so we create a Expression for high priority term and other one for start of term until here.
                    newTerm = Exception(term[startIndex:i])
                    self.term.append(newTerm)
                    newTerm = Exception(self.term)
                    self.term.clear()
                    self.term.append(newTerm)
                    self.term.append(term[i])
                    thisPriority = newPriority
            i += 1
        self.cleanParentheses()
