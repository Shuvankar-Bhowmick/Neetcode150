'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we need a hashmap to store the strings
        map = defaultdict(list)
        for str in strs:
            # create an array and store the count of the characters
            # present in the string, in the array
            arr = [0] * 26
            for ch in str:
                arr[ord(ch) - ord('a')] += 1
            key = tuple(arr)
            map[key].append(str)

        ans = [value for value in map.values()]
        return ans
                