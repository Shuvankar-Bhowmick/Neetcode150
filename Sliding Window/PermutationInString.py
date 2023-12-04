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
        set1, set2 = defaultdict(int), defaultdict(int)
        length = len(set1)
        matches = 0
        
        # Fill set1
        for ch in s1:
            set1[ch] += 1
        # Fill set2
        for ch in s2:
            set2[ch] += 1
            if set2[ch] == set1[ch]:
                matches += 1        
        
        if matches == length:
            return True
        
        l = 0
        for r in range(length, len(s2)):
            if matches == length:
                return True
            
            if set2[s2[l]] == set1[s2[l]]:
                matches -= 1
            
            set2[s2[l]] -= 1
            set2[s2[r]] += 1
            if set2[s2[r]] == set1[s2[r]]:
                matches += 1
                
        return False        
                
            
            
                    