'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
'''
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {'+', '-', '/', '*'}:
                secondNum = int(stack.pop())
                firstNum = int(stack.pop())
                if token == '+':
                    stack.append(firstNum + secondNum)
                elif token == '-':
                    stack.append(firstNum - secondNum)
                elif token == '/':
                    stack.append(firstNum / secondNum)
                else:
                    stack.append(firstNum * secondNum)
            else:
                stack.append(token)

        return stack[0]                

        