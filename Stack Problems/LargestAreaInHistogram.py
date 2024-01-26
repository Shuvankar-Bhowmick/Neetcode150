'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for h in heights:
            currIndex = 0
            i = len(stack) - 1
            while h < stack[i]:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index + 1) * height)
                i -= 1    
            currIndex = i + 1 if stack else 0
            stack.append((currIndex, h))
        
        while stack:
            