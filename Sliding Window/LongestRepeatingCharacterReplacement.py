'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxWindow = 0
        count = dict()
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            maxWindow = max(r - l + 1, maxWindow)    

        return maxWindow        
                        
