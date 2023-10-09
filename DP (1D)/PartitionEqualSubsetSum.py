'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:    
'''
from functools import reduce
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # bottom-top iterative approach
        target = reduce(lambda x, y: x + y, nums)
        if target & 1: 
            return False
        target //= 2

        dp = {0}
        for i in range(len(nums) - 1):
            # include the element
            temp = dp.copy()
            for val in temp:
                dp.add(val + nums[i])
                if target in dp:
                    return True
        return False            