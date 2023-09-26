'''
Given a string s, return the longest 
palindromic substring in s.
'''

class Solution:
    __starting_index = 0
    __max_starting_index = 0
    max_length = 0

    def longestPalindrome(self, s: str) -> str:
        # we fill run a loop through the entire string
        # the i will go to every index and every index will be treated as the middle
        # of a susbstring as long as it stays inside bounds
        for i in range(len(s)):
            lenEven = self.find_even_palindrome(i, s)
            if lenEven > self.max_length:
                self.max_length = lenEven
                self.__max_starting_index = self.__starting_index
        
        for i in range(len(s)):
            lenOdd = self.find_odd_palindrome(i, s)
            if lenOdd > self.max_length:
                self.max_length = lenOdd
                self.__max_starting_index = self.__starting_index

        return s[self.__max_starting_index: self.max_length + self.__max_starting_index]    
    
    def find_odd_palindrome(self, index, str):
        i = j = index
        while (i >= 0 and j < len(str)
               and 
               str[i] == str[j]):
            i -= 1
            j += 1

        self.__starting_index = i + 1
        return j - i - 1  
    
    def find_even_palindrome(self, index, str):
        i = index
        j = index + 1
        while (i >= 0 and j < len(str) and
               str[i] == str[j]):
            i -= 1
            j += 1
        self.__starting_index = i + 1    
        return j - i - 1    
