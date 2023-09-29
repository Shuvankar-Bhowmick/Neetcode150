'''
Given an integer array nums, find a 
subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minNum = 1
        maxNum = 1
        res = max(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                minNum = maxNum = 1
            else:    
                temp = minNum
                minNum = min(maxNum * nums[i], nums[i], minNum * nums[i])
                maxNum = max(temp * nums[i], nums[i], maxNum * nums[i])  
                res = max(res, minNum, maxNum) 

        return res
        
sol = Solution()
print(sol.maxProduct([-3, -1, -1]))    