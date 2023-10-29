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
        target = reduce(lambda x, y: x + y, nums)
        if target % 2 != 0: 
            return False
        target //= 2
        N, M = len(nums) + 1, target + 1
        dp = [[False] * M for _ in range(N)]
        dp[0][0] = True

        for r in range(1, N):
            for c in range(0, M):
                # skipping the element
                skip = dp[r - 1][c]
                # including the element
                include = False
                if c >= nums[r - 1]:
                    include = dp[r - 1][c - nums[r - 1]]
                dp[r][c] = skip or include 

        return dp[N - 1][M - 1]

solution = Solution()
print(solution.canPartition([1,5,11,5]))    