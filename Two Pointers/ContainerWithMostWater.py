'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res, maxRes = 0, 0
    
        while left < right:
            res = (right - left) * min(height[left], height[right])
            maxRes = max(maxRes, res)

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1

        return maxRes            