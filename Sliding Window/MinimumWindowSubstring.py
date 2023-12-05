'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # len(t) must be <= len(s)
        if len(t) > len(s): return ""
        
        minLength = float("inf")
        res = ""
        haveCount = dict()
        needCount = dict()
        for ch in t:
            needCount[ch] = needCount.get(ch, 0) + 1
        count = len(needCount)

        l = 0
        for r in range(len(s)):
            haveCount[s[r]] = haveCount.get(s[r], 0) + 1
            if s[r] in needCount and haveCount[s[r]] == needCount[s[r]]:
                count -= 1
            
            while count == 0:
                # found a match
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    res = s[l: l + minLength]

                # look for a smaller window
                # pop from the left
                haveCount[s[l]] -= 1
                if s[l] in needCount and haveCount[s[l]] < needCount[s[l]]:
                    count += 1
                l += 1

        return res
    
solution = Solution()
print(solution.minWindow("cabwefgewcwaefgcf","cae"))    
                




                


        

