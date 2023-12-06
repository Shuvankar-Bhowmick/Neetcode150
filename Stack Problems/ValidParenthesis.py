'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in openToClose:
                if stack and openToClose[ch] == stack[-1]:  # top = stack[-1]
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if len(stack) == 0 else False                    