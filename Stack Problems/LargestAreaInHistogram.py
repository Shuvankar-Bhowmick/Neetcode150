'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                # pop the stack
                index, height = stack.pop()
                # calculate the max area
                maxArea = max(maxArea, (i - index) * height)
                start = index
            stack.append((start, h))
        end = len(heights)
        while stack:
            index, height = stack.pop()                        
            maxArea = max(maxArea, (end - index) * height)
        return maxArea

solution = Solution()
print(solution.largestRectangleArea([2,1,2]))