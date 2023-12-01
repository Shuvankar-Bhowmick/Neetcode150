'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        i = 0
        while i < (len(nums) - 2):
            
            if nums[i] > 0: break

            # To make sure there's no duplicates for i        
            while (i > 0 and nums[i] == nums[i - 1]): i += 1

            j,  k = i + 1, len(nums) - 1
            while (j < k):
                if nums[i] + nums[j] + nums[k] == 0:
                    # must ensure that duplicate elements are not added to the ans
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while (j < k and nums[j] == nums[j - 1]): j += 1
                    while (j < k and nums[k] == nums[k + 1]): k -= 1 
                
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                
                else:
                    j += 1
            i += 1    

        return ans                   
            
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))    
print(solution.threeSum([0,1,1]))    
print(solution.threeSum([0, 0, 0]))    