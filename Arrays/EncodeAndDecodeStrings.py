'''
Problem link: https://www.lintcode.com/problem/659/description
'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        print(encodedStr)
        return encodedStr

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        decodedStr = []
        i = 0
        while i in range(len(str)):
            
            
        decodedStr.append(temp)
        print(decodedStr)
        return decodedStr
    
solution = Solution()
encodedStr = solution.encode(["lint","co-de", "#love","you", "", "#", "5"])
decodedStr = solution.decode(encodedStr)

# print(f"Output: {decodedStr}")    