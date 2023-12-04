'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
'''

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        s1Count, s2Count = defaultdict(int), defaultdict(int)
        matches = 0
        # Iterate through the first string
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1

        length = len(s1Count)
        
        for key in s1Count.keys():
            if s1Count[key] == s2Count[key]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == length:
                return True
            
            # check for the right pointer
            s2Count[s2[r]] += 1
            if s2Count[s2[r]] == s1Count[s2[r]]:
                matches += 1
            if (s2Count[s2[r]] == s1Count[s2[r]] + 1) and (s1Count[s2[r]] != 0):
                matches -= 1

            # check for the left pointer
            s2Count[s2[l]] -= 1
            if (s2Count[s2[l]] == s1Count[s2[l]]) and (s1Count[s2[l]] != 0):
                matches += 1
            if s2Count[s2[l]] == s1Count[s2[l]] - 1:
                matches -= 1
            l += 1

        return True if matches == length else False

solution = Solution()
# print("Answer:", solution.checkInclusion("ab","eidboaoo"))         
print("Answer:", solution.checkInclusion("ab",
"eidboaoo"))         
                    