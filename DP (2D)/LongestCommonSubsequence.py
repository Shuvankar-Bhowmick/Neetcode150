'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        # memoization
        # def lcs(r, c):
        #     if r == 0 or c == 0:
        #         return 0
        #     if dp[r][c] != -1:
        #         return dp[r][c]
            
        #     if text1[r - 1] == text2[c - 1]:
        #         dp[r][c] = 1 + lcs(r-1, c-1)
        #     else:
        #         dp[r][c] = max(lcs(r, c-1), lcs(r-1, c))

        #     return dp[r][c]

        # return lcs(rows, cols)          
        
        # --------------------------------------------------------------- 
        # Tabulation
        for i in range(1, rows):
            for j in range(1, cols):

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[rows - 1][cols - 1]                 