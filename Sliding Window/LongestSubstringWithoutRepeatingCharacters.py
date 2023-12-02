class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = float('-inf')
        charSet = set()
        start = 0

        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(s[end])
            maxLength = max(maxLength, end - start + 1)

        return 0 if maxLength == float('-inf') else int(maxLength)
    
solution = Solution()   
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring(" "))
print(solution.lengthOfLongestSubstring(""))