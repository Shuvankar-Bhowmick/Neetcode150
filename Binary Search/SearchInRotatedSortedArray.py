'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Find out if the target lies on the left of the pivot or the right
        # 2. Once that is found, adjust your left and right pointers accordingly.
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # check if it is in the left half of the pivot
            if nums[mid] >= nums[l]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # check the right half of the pivot
            else:
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        
solution = Solution()
print(solution.search([4,5,6,7,0,1,2],0))                            
print(solution.search([4,5,6,7,0,1,2],3))                            
print(solution.search([1],0))                            
print(solution.search([1, 3],3))                            
print(solution.search([1, 3],1))                            
print(solution.search([3, 1],3))                            
print(solution.search([3, 1],1))                            

                        