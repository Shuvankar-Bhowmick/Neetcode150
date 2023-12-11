'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        openCount, closeCount = 0, 0

        def backtracking(openCount, closeCount):
            if openCount == closeCount == n:
                res.append("".join(stack))
                return
            
            if openCount < n:
                stack.append("(")
                backtracking(openCount + 1, closeCount)
                stack.pop()

            elif closeCount < openCount:
                stack.append(")")
                backtracking(openCount, closeCount + 1)
                stack.pop()
                
            return 
        backtracking(openCount, closeCount)
        return res        


