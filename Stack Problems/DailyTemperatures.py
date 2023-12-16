'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Enter the number and its indices in the stack
        stack = []
        ans = [0 for _ in range(len(temperatures))]
        
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                _, index = stack.pop()
                ans[index] = i - index
                
            stack.append(n)
        return ans            