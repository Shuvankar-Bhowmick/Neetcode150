'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0

        for n in num1:
            n1 = n1 * 10 + (ord(n) - ord("0"))
        for n in num2:
            n2 = n2 * 10 + (ord(n) - ord("0"))    

        return str(n1 * n2)    
