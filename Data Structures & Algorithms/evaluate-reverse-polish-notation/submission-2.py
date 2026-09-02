import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', "-", "*", "/"]

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if token == '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                elif token == '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                elif token == '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a*b)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a/b))
        
        result = stack.pop()
        return result
        